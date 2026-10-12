# Hummingbot maintenance verification

## Final launcher repair and verification

Source commit `a5f86d495` fixes wheel-installed quickstart ownership and declares its interactive runtime dependencies. The final Python 3.15 wheel contains **61 native extensions and 904 Python modules**. Both installed console help commands passed from `/tmp` in a separate frozen environment, and all original launcher function/class bodies are unchanged. The source compatibility wrapper, strict compilation, wheel and sdist build also passed. The 380 existing CLI/client-runner cases passed during the repair. An independent read-only agent review found no actionable defects in the launcher commit and confirmed wheel modules match source, correct package entrypoints and unchanged tests. The fresh complete existing suite on source `a5f86d4953c6b93c472cbda80a4c74ed0c06ba7a` passed: **8,802 passed, one unchanged skip and two subtests passed**, in 870.52 seconds pytest time (878.45 seconds command wall time), exit 0. The source snapshot was clean at command start. No test cases or assertions changed in this launcher follow-up. The earlier complete-suite result below remains historical evidence.

The supported commands and package owners are documented in [development](development.md), including [interactive](../src/hummingbot/client/interactive.py) and [quickstart](../src/hummingbot/client/quickstart.py).

## Earlier complete-suite outcome

The complete existing suite passed on managed Python 3.15.0: **8,802 passed, one pre-existing skip, and two subtests passed**, exit 0, in 901.32 seconds. No new test cases were added. The unchanged skipped trade-monitor case documents an upstream hang; it was already skipped before this maintenance.

Source commit: `26690d28eaefd6e89605c1fe562d8b77aa5660b7`. The source exercised by the final test run was then committed at this revision; the native wheel includes the final production cache-key fix. This earlier run predates the packaged launcher follow-up described above.

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

[Portable verification records](maintenance/verification.json) retain exact commands, exit codes, durations and original-log hashes. [Readable evidence index](maintenance/index.md) includes earlier failed experiments as well as the final passing run. The current final full-suite log is `hummingbot-final-packaged-launcher-complete-existing-suite.log` in the workspace maintenance evidence.

This proves the existing local suite and native wheel build. It does not claim authenticated live trading or production deployment. The existing live-service requirements and original skip remain visible.
