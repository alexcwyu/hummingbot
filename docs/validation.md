# Hummingbot maintenance verification

## Final outcome

The complete existing suite passed on managed Python 3.15.0: **8,802 passed, one pre-existing skip, and two subtests passed**, exit 0, in 901.32 seconds. No new test cases were added. The unchanged skipped trade-monitor case documents an upstream hang; it was already skipped before this maintenance.

Source commit: `26690d28eaefd6e89605c1fe562d8b77aa5660b7`. The source exercised by the final test run was then committed at this revision; the native wheel includes the final production cache-key fix. Subsequent changes are documentation only.

```sh
.venv/bin/python -m pytest test --tb=short
.venv/bin/python -W error -m compileall -q src controllers scripts vendor test/conftest.py
```

The Python 3.15 wheel contains **61 compiled native modules and 902 Python modules**, including package resources. The wheel build, inventory check and strict source compilation passed. Rebuild native extensions after source changes; a syntax-only check cannot establish native build success.

## Repairs and preserved contracts

- The [asynchronous TTL cache](../src/hummingbot/core/utils/__init__.py) retains real hashable arguments and instance identity, preventing a newly allocated connector from reusing an old connector's cached result.
- The [resource fixture](../test/conftest.py) observes both event-loop constructors, cancels only newly allocated tasks, awaits their finalizers, and closes only owned loops and network/database resources. It preserves pre-existing tasks on external loops.
- Existing [BTC Markets lifecycle tests](../test/hummingbot/data_feed/candles_feed/btc_markets_spot_candles/test_btc_markets_spot_candles.py) now mock both HTTP boundaries using the existing candle data. All 79 original test methods and 128 original unittest assertions are preserved; no synthetic lifecycle events replace callbacks.
- Python 3.15 dependency repairs retain upstream source and licenses. See [development and dependency provenance](development.md), including private protobuf descriptor pools that allow the original Injective and dYdX schemas to coexist without altering their wire definitions.

## Evidence and limits

[Portable verification records](maintenance/verification.json) retain exact commands, exit codes, durations and original-log hashes. [Readable evidence index](maintenance/index.md) includes earlier failed experiments as well as the final passing run. The final full-suite log is `hummingbot-resumed-final-existing-full-tests.log` in the workspace maintenance evidence.

This proves the existing local suite and native wheel build. It does not claim authenticated live trading or production deployment. The existing live-service requirements and original skip remain visible.
