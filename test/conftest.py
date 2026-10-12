"""Own legacy unittest loops and release database resources on current Python."""
import asyncio
import time
import unittest

import aiohttp

import pytest
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


def _drain_tasks(loop, tasks, timeout=10):
    for task in tasks:
        task.cancel()
    if tasks:
        pending = asyncio.gather(*tasks, return_exceptions=True)
        deadline = time.monotonic() + timeout
        timer = loop.call_later(timeout, loop.stop)
        try:
            while not pending.done():
                if time.monotonic() >= deadline:
                    unfinished = [repr(task) for task in tasks if not task.done()]
                    raise RuntimeError(f"Test tasks did not stop within 10 seconds: {unfinished}")
                try:
                    loop.run_until_complete(pending)
                except RuntimeError as error:
                    # Some gRPC callbacks stop the loop during cancellation. Retry
                    # only within the deadline, preserving unfinished-task failures.
                    if str(error) != "Event loop stopped before Future completed.":
                        raise
        finally:
            timer.cancel()


def _drain_allocated_tasks(loop, baseline):
    deadline = time.monotonic() + 10
    while tasks := asyncio.all_tasks(loop) - baseline:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise RuntimeError(f"Test tasks kept spawning during shutdown: {[repr(task) for task in tasks]}")
        _drain_tasks(loop, tasks, timeout=remaining)


def _close_loop(loop):
    if loop.is_closed() or loop.is_running():
        return
    _drain_tasks(loop, asyncio.all_tasks(loop))
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()


@pytest.fixture(scope="class", autouse=True)
def unittest_class_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    _close_loop(loop)
    asyncio.set_event_loop(None)


@pytest.fixture(autouse=True)
def release_test_resources(monkeypatch):
    # Python 3.14 no longer creates an implicit default loop. Old unittest
    # setup methods still use get_event_loop(), so supply an explicitly owned one.
    owned_loop = None
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        owned_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(owned_loop)
    default_loop = asyncio.get_event_loop()
    task_baselines = {default_loop: asyncio.all_tasks(default_loop)}
    new_event_loop = asyncio.new_event_loop
    allocated_loops = set()

    def tracked_new_event_loop():
        loop = new_event_loop()
        # This fixture observed its creation, so all later tasks belong to the
        # test. Existing external loops instead get a conservative snapshot.
        task_baselines[loop] = set()
        allocated_loops.add(loop)
        install_close_hook(loop)
        return loop

    monkeypatch.setattr(asyncio, "new_event_loop", tracked_new_event_loop)
    # asyncio.Runner and unittest use the events module entry point directly.
    monkeypatch.setattr(asyncio.events, "new_event_loop", tracked_new_event_loop)
    engines = []
    sessions = []
    http_sessions = []
    http_init = aiohttp.ClientSession.__init__
    http_loop_closers = set()

    async def close_owned_http(loop):
        owned = [session for session in http_sessions if session._loop is loop]
        for session in owned:
            if not session.closed:
                await session.close()
        if owned:
            # Session.close schedules TLS transport shutdown on its owning loop.
            # Even an already-closed session needs that loop alive to finish it.
            await asyncio.sleep(0.25)

    def install_close_hook(loop):
        if loop not in http_loop_closers:
            http_loop_closers.add(loop)
            original_close = loop.close

            def close_with_owned_http():
                if not loop.is_closed() and not loop.is_running():
                    # Runner cancellation can spawn finalizer tasks after its
                    # initial task snapshot. Drain those before closing HTTP.
                    _drain_allocated_tasks(loop, task_baselines[loop])
                    loop.run_until_complete(close_owned_http(loop))
                original_close()

            # Intercept only newly created test loops or loops owning HTTP
            # sessions allocated by this fixture, preserving existing tasks.
            monkeypatch.setattr(loop, "close", close_with_owned_http)

    def tracked_http_init(self, *args, **kwargs):
        http_init(self, *args, **kwargs)
        http_sessions.append(self)
        loop = self._loop
        # A session may use an existing nondefault loop. Preserve the tasks
        # already on it instead of inferring ownership from the session alone.
        if loop not in task_baselines:
            task_baselines[loop] = asyncio.all_tasks(loop)
        install_close_hook(loop)

    monkeypatch.setattr(aiohttp.ClientSession, "__init__", tracked_http_init)
    engine_init = Engine.__init__
    session_init = Session.__init__

    def tracked_engine_init(self, *args, **kwargs):
        engine_init(self, *args, **kwargs)
        engines.append(self)

    def tracked_session_init(self, *args, **kwargs):
        session_init(self, *args, **kwargs)
        sessions.append(self)

    monkeypatch.setattr(Engine, "__init__", tracked_engine_init)
    monkeypatch.setattr(Session, "__init__", tracked_session_init)
    yield
    for loop, baseline in task_baselines.items():
        if not loop.is_closed() and not loop.is_running():
            # Stop this test's background requests before session.close. Closing
            # sessions while their connect tasks are alive can leave transports
            # that complete after HTTP cleanup on a shared class loop.
            _drain_allocated_tasks(loop, baseline)
    for session in sessions:
        session.close()
    http_loops = {session._loop for session in http_sessions}
    for loop in http_loops:
        if not loop.is_closed() and not loop.is_running():
            for session in http_sessions:
                if session._loop is loop and not session.closed:
                    loop.run_until_complete(session.close())
            loop.run_until_complete(asyncio.sleep(0.25))
    for engine in engines:
        engine.dispose()
    for loop in allocated_loops:
        _close_loop(loop)
    try:
        current_loop = asyncio.get_event_loop()
    except RuntimeError:
        current_loop = None
    if current_loop in allocated_loops:
        asyncio.set_event_loop(default_loop if not default_loop.is_closed() else None)
    if owned_loop is not None:
        _close_loop(owned_loop)
    if owned_loop is not None:
        asyncio.set_event_loop(None)
