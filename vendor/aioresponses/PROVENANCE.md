# aiohttp response fixture compatibility

This is the MIT-licensed aioresponses 0.7.9 release source. [Official source](https://github.com/pnuckowski/aioresponses/blob/0.7.9/aioresponses/core.py) constructs `ClientResponse` without the `stream_writer` keyword required by aiohttp 3.14.5. The local `0.7.9+ayu.1` source detects this public constructor parameter and supplies a zero-byte mock writer. HTTP matching, callbacks and assertions remain unchanged; no existing test cases or warning checks are removed. Remove this source when the published library supports the new constructor.

`compat.stream_reader_factory` uses a fixture response protocol that tracks pause/resume state for an already-decoded body. Current aiohttp forwards flow control to an active HTTP parser; fixture bodies have no socket/parser, so they need only the reader pause state. Large mocked responses remain fully readable. Response matching/callback semantics and all existing host assertions are preserved.
