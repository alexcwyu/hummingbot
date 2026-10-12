# hummingbot: portable verification records

These records retain exact commands, outcomes, original-log hashes and available source snapshots. Failed, interrupted and earlier exploratory commands remain visible. A later focused pass proves only its own scope.

[Machine-readable records](verification.json) · [Validation](../validation.md) · [Engineering guide](../ayu-develop.md)

Original logs remain in the workspace maintenance evidence. Tracked source hashes exclude untracked additions and later edits, as stated in each captured snapshot.

| Check | Exit | Duration | Command |
| --- | ---: | ---: | --- |
| async-fixture-focused-tests-2 | 0 | 2.6s | `.venv/bin/python -m pytest test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_exchange.py::CoinbaseAdvancedTradeExchangeTests::test_lost_order_included_in_order_fills_update_and_not_in_order_status_update test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_exchange.py::CoinbaseAdvancedTradeExchangeTests::test_update_order_status_when_canceled test/hummingbot/connector/derivative/grvt_perpetual/test_grvt_perpetual_derivative.py::GrvtPerpetualDerivativeUnitTests test/hummingbot/connector/test_time_synchronizer.py --tb=short` |
| async-fixture-focused-tests | 1 | 2.9s | `.venv/bin/python -m pytest test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_exchange.py::CoinbaseAdvancedTradeExchangeTests::test_lost_order_included_in_order_fills_update_and_not_in_order_status_update test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_exchange.py::CoinbaseAdvancedTradeExchangeTests::test_update_order_status_when_canceled test/hummingbot/connector/derivative/grvt_perpetual/test_grvt_perpetual_derivative.py::GrvtPerpetualDerivativeUnitTests --tb=short` |
| async-interface-focused-tests | 1 | 21.86s | `.venv/bin/python -m pytest test/hummingbot/connector/test_connector_base.py test/hummingbot/connector/exchange/derive/test_derive_auth.py test/hummingbot/connector/exchange/foxbit/test_foxbit_user_stream_data_source.py test/hummingbot/connector/exchange/ndax/test_ndax_auth.py test/hummingbot/strategy/spot_perpetual_arbitrage/test_spot_perpetual_arbitrage_start.py test/hummingbot/strategy/avellaneda_market_making/test_avellaneda_market_making_start.py test/hummingbot/connector/derivative/kucoin_perpetual/test_kucoin_perpetual_derivative.py test/hummingbot/connector/exchange/xrpl/test_xrpl_transaction_pipeline.py test/hummingbot/connector/exchange/xrpl/test_xrpl_utils.py --tb=short` |
| build-dependency-sync | 1 | 6.06s | `uv sync --all-extras --python 3.14` |
| build | 0 | 12.99s | `uv build --python 3.13` |
| cancel-order-focused-tests | 0 | 3.3s | `.venv/bin/python -m pytest test/hummingbot/connector/exchange/binance/test_binance_exchange.py::BinanceExchangeTests::test_cancel_two_orders_with_cancel_all_and_one_fails test/hummingbot/connector/derivative/architect_perpetual/test_architect_perpetual_derivative.py::ArchitectPerpetualDerivativeUnitTest::test_cancel_two_orders_with_cancel_all_and_one_fails --tb=short` |
| candles-poll-existing-tests | 1 | 20.75s | `.venv/bin/python -m pytest test/hummingbot/data_feed/candles_feed/btc_markets_spot_candles --tb=short` |
| compatible-sync-2 | 0 | 508.03s | `uv sync --all-extras --python 3.14` |
| compatible-sync-3 | 0 | 415.73s | `uv sync --all-extras --python 3.14` |
| compile | 0 | 0.93s | `<workspace>/hummingbot/.venv/bin/python -m compileall -q src` |
| conservative-ownership-focused-tests | 0 | 43.48s | `.venv/bin/python -m pytest test/hummingbot/data_feed/candles_feed/btc_markets_spot_candles test/test_isolated_asyncio_wrapper_test_case.py test/test_logger_mixin_for_test.py test/hummingbot/connector/derivative/bitmart_perpetual test/hummingbot/connector/derivative/evedex_perpetual --tb=short` |
| core315-tests | 1 | 34.23s | `.venv/bin/python -m pytest test/hummingbot/core test/hummingbot/strategy` |
| coroutine-allocation-diagnostic-tests | 1 | 71.36s | `env PYTHONTRACEMALLOC=15 .venv/bin/python -m pytest test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_exchange.py::CoinbaseAdvancedTradeExchangeTests::test_lost_order_included_in_order_fills_update_and_not_in_order_status_update test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_exchange.py::CoinbaseAdvancedTradeExchangeTests::test_update_order_status_when_canceled test/hummingbot/connector/derivative/grvt_perpetual/test_grvt_perpetual_derivative.py --tb=short` |
| corrected-quickstart-console-help | 0 | 2.52s | `uv run --frozen --all-extras hummingbot_quickstart --help` |
| corrected-source-wrapper-help | 0 | 2.51s | `uv run --frozen --all-extras python bin/hummingbot_quickstart.py --help` |
| corrected-sync | 1 | 2.25s | `uv sync --all-extras --python 3.14` |
| current-api-final-focused-tests-2 | 1 | 34.48s | `.venv/bin/python -m pytest test/hummingbot/connector/derivative/dydx_v4_perpetual test/hummingbot/connector/exchange/injective_v2 test/hummingbot/connector/exchange/foxbit/test_foxbit_user_stream_data_source.py test/hummingbot/connector/exchange/foxbit/test_foxbit_utils.py test/hummingbot/client/command/test_config_command.py --tb=short` |
| current-api-final-focused-tests | 1 | 18.91s | `.venv/bin/python -m pytest test/hummingbot/connector/derivative/dydx_v4_perpetual test/hummingbot/connector/exchange/foxbit/test_foxbit_user_stream_data_source.py test/hummingbot/client/command/test_config_command.py --tb=short` |
| current-api-focused-tests-2 | 1 | 27.51s | `.venv/bin/python -m pytest test/hummingbot/core/test_trading_core.py test/hummingbot/core/utils/test_tracking_nonce.py test/hummingbot/core/utils/test_estimate_fee.py test/hummingbot/connector/derivative/lighter_perpetual/test_lighter_perpetual_derivative.py test/hummingbot/connector/exchange/gemini/test_gemini_exchange.py` |
| current-api-focused-tests-3 | 0 | 51.14s | `.venv/bin/python -m pytest test/hummingbot/core/test_trading_core.py test/hummingbot/core/utils/test_tracking_nonce.py test/hummingbot/core/utils/test_estimate_fee.py test/hummingbot/connector/derivative/lighter_perpetual/test_lighter_perpetual_derivative.py test/hummingbot/connector/exchange/gemini/test_gemini_exchange.py` |
| current-api-focused-tests | 1 | 22.13s | `.venv/bin/python -m pytest test/hummingbot/core/test_trading_core.py test/hummingbot/core/utils/test_tracking_nonce.py test/hummingbot/core/utils/test_estimate_fee.py test/hummingbot/connector/derivative/lighter_perpetual/test_lighter_perpetual_derivative.py` |
| current-full-tests | 1 | 951.07s | `.venv/bin/python -m pytest test --continue-on-collection-errors` |
| current-native-build-2 | 0 | 129.47s | `uv build --python 3.15` |
| current-native-sync | 0 | 139.36s | `uv sync --all-extras --frozen --python 3.15 --reinstall-package hummingbot` |
| current-sync | 0 | 146.87s | `uv sync --all-extras --python 3.14` |
| default-loop-resource-focused-tests | 0 | 8.77s | `.venv/bin/python -m pytest test/hummingbot/cli test/hummingbot/client/test_runner.py test/hummingbot/client/ui --tb=short` |
| final-current-tests | 1 | 675.13s | `.venv/bin/python -m pytest test --continue-on-collection-errors` |
| final-existing-full-tests | -15 | 655.48s | `.venv/bin/python -m pytest test --continue-on-collection-errors --tb=short -o faulthandler_timeout=60` |
| final-fallback-sync | 0 | 96.0s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-installed-wheel-console-help | 0 | 5.18s | `/tmp/trading-humming-final-wheel315/bin/hummingbot_quickstart --help` |
| final-installed-wheel-hbot-help | 0 | 0.45s | `/tmp/trading-humming-final-wheel315/bin/hbot --help` |
| final-installed-wheel-isolated-import | 1 | 1.54s | `/tmp/trading-humming-final-wheel315/bin/python -I -c import hummingbot, hummingbot.client.interactive, hummingbot.client.quickstart, sys; from pathlib import Path; p=Path(hummingbot.__file__).resolve(); assert str(p).startswith("/tmp/trading-humming-final-wheel315/"); assert "<workspace>/hummingbot/src" not in sys.path; print(p); print(sys.version)` |
| final-installed-wheel-isolated-realpath-import | 0 | 1.68s | `/tmp/trading-humming-final-wheel315/bin/python -I -c import hummingbot, hummingbot.client.interactive, hummingbot.client.quickstart, sys; from pathlib import Path; p=Path(hummingbot.__file__).resolve(); expected=Path("/tmp/trading-humming-final-wheel315").resolve(); assert p.is_relative_to(expected), (p, expected); assert "<workspace>/hummingbot/src" not in sys.path; print(p); print(sys.version)` |
| final-isolated-wheel-install | 0 | 0.19s | `uv pip install --python /tmp/trading-humming-final-wheel315/bin/python --no-deps --reinstall <workspace>/hummingbot/dist/hummingbot-2.17.0-cp315-cp315-macosx_11_0_arm64.whl` |
| final-lock | 0 | 1.95s | `uv lock --upgrade` |
| final-native-build-2 | 0 | 97.7s | `uv build` |
| final-native-build | 0 | 98.55s | `uv build --python 3.15.0` |
| final-native-tests | 0 | 4.3s | `.venv/bin/python -m pytest test/hummingbot/core/test_pubsub.py test/hummingbot/core/data_type/test_order_book.py test/hummingbot/core/test_clock.py` |
| final-observed-existing-tests-2 | -15 | 243.9s | `env BOTS_REPO=hummingbot .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['test','--continue-on-collection-errors','--tb=short','-p','bots_test_observer','-o','faulthandler_timeout=60']))` |
| final-observed-existing-tests-3 | 1 | 950.24s | `env BOTS_REPO=hummingbot .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['test','--continue-on-collection-errors','--tb=short','-p','bots_test_observer','-o','faulthandler_timeout=60']))` |
| final-observed-existing-tests | 1 | 926.86s | `env BOTS_REPO=hummingbot .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['test','--continue-on-collection-errors','--tb=short','-p','bots_test_observer','-o','faulthandler_timeout=60']))` |
| final-packaged-launcher-complete-existing-suite | 0 | 878.45s | `uv run --frozen --all-extras python -m pytest test --tb=short` |
| final-packaged-launcher-strict-source-compile | 0 | 0.49s | `uv run --frozen --all-extras python -W error -m compileall -q src controllers scripts vendor bin test/conftest.py` |
| final-packaged-launcher-wheel-and-sdist-build | 0 | 81.51s | `uv build --python 3.15` |
| final-resource-contract-tests | 0 | 89.35s | `.venv/bin/python -m pytest test/hummingbot/cli test/hummingbot/client/ui test/hummingbot/client/test_runner.py test/hummingbot/connector/derivative/gate_io_perpetual test/hummingbot/connector/derivative/grvt_perpetual test/hummingbot/connector/exchange/coinbase_advanced_trade test/hummingbot/connector/exchange/gemini test/hummingbot/connector/test_time_synchronizer.py --tb=short` |
| final-resource-focused-tests-3 | -15 | 155.39s | `.venv/bin/python -m pytest test/hummingbot/connector/exchange/foxbit test/hummingbot/connector/exchange/injective_v2 test/hummingbot/connector/derivative/dydx_v4_perpetual test/hummingbot/connector/derivative/injective_v2_perpetual test/hummingbot/client/command/test_config_command.py --tb=short -o faulthandler_timeout=30` |
| final-resource-focused-tests-4 | 0 | 61.72s | `.venv/bin/python -m pytest test/hummingbot/connector/exchange/foxbit test/hummingbot/connector/exchange/injective_v2 test/hummingbot/connector/derivative/dydx_v4_perpetual test/hummingbot/connector/derivative/injective_v2_perpetual test/hummingbot/client/command/test_config_command.py --tb=short -o faulthandler_timeout=30` |
| final-resource-focused-tests | -15 | 208.0s | `.venv/bin/python -m pytest test/hummingbot/connector/exchange/foxbit test/hummingbot/connector/exchange/injective_v2 test/hummingbot/connector/derivative/dydx_v4_perpetual test/hummingbot/connector/derivative/injective_v2_perpetual test/hummingbot/client/command/test_config_command.py --tb=short` |
| final-strict-compile-2 | 0 | 0.86s | `.venv/bin/python -W error -m compileall -q src controllers scripts vendor test/conftest.py` |
| final-strict-compile-3 | 0 | 0.64s | `.venv/bin/python -W error -m compileall -q src controllers scripts vendor test/conftest.py` |
| final-strict-compile | 0 | 0.81s | `.venv/bin/python -W error -m compileall -q src controllers scripts vendor test/conftest.py` |
| final-sync | 0 | 204.99s | `env TA_INCLUDE_PATH=/opt/homebrew/opt/ta-lib/include TA_LIBRARY_PATH=/opt/homebrew/opt/ta-lib/lib uv sync --all-extras --python 3.15` |
| final-tests | 2 | 14.73s | `.venv/bin/python -m pytest test` |
| final-wheel-inventory-2 | 0 | 0.08s | `.venv/bin/python -c from pathlib import Path;import zipfile;w=max(Path('dist').glob('*.whl'),key=lambda p:p.stat().st_mtime);z=zipfile.ZipFile(w);names=z.namelist();native=[n for n in names if n.endswith('.so')];python=[n for n in names if n.endswith('.py')];assert len(native)==61;assert len(python)==902;assert 'hummingbot/VERSION' in names;assert not any('/__pycache__/' in n for n in names);print(w.name,'native modules',len(native),'Python modules',len(python),'size',w.stat().st_size)` |
| final-wheel-inventory | 0 | 0.09s | `.venv/bin/python -c from pathlib import Path;import zipfile;w=max(Path('dist').glob('*.whl'),key=lambda p:p.stat().st_mtime);z=zipfile.ZipFile(w);names=z.namelist();native=[n for n in names if n.endswith('.so')];python=[n for n in names if n.endswith('.py')];assert len(native)==61;assert len(python)==902;assert 'hummingbot/VERSION' in names;assert not any('/__pycache__/' in n for n in names);print(w.name,'native modules',len(native),'Python modules',len(python),'size',w.stat().st_size)` |
| final-wheel-isolated-runtime-sync | 0 | 1.31s | `env UV_PROJECT_ENVIRONMENT=/tmp/trading-humming-final-wheel315 uv sync --frozen --all-extras --python 3.15` |
| formatted-config-focused-tests | 1 | 5.35s | `.venv/bin/python -m pytest test/hummingbot/client/command/test_config_command.py::ConfigCommandTest::test_list_configs_pydantic_model --tb=short` |
| full-current-tests | 1 | 157.88s | `.venv/bin/python -m pytest test --continue-on-collection-errors` |
| full315-collection | 2 | 15.47s | `.venv/bin/python -m pytest test --collect-only` |
| full315-tests | 1 | 220.23s | `.venv/bin/python -m pytest test --continue-on-collection-errors` |
| imported-source-whitespace | 0 | 0.85s | `.venv/bin/python /tmp/bots-normalize-import-whitespace.py` |
| installed-legacy-console-help | 1 | 0.25s | `uv run --frozen --all-extras hummingbot_quickstart --help` |
| latest-pandas-sync | 0 | 110.8s | `env TA_INCLUDE_PATH=/opt/homebrew/opt/ta-lib/include TA_LIBRARY_PATH=/opt/homebrew/opt/ta-lib/lib uv sync --all-extras --python 3.15` |
| latest-vendor-compile | 0 | 1.24s | `.venv/bin/python -W error -m compileall -q -f vendor` |
| legacy-fixture-tests-2 | 1 | 42.68s | `.venv/bin/python -m pytest test/hummingbot/core test/hummingbot/strategy` |
| legacy-fixture-tests | 2 | 3.56s | `.venv/bin/python -m pytest test/hummingbot/core test/hummingbot/strategy` |
| lighter-final-sync | 0 | 121.47s | `uv sync --all-extras --frozen --python 3.15` |
| lighter-source-lock | 0 | 2.7s | `uv lock --upgrade` |
| lock-3.13 | 0 | 0.87s | `uv lock --upgrade --python 3.13` |
| lock-3.14 | 0 | 0.41s | `uv lock --upgrade --python 3.14` |
| lock-3.15 | 0 | 14.71s | `uv lock --upgrade --python 3.15` |
| native315-core | 4 | 0.61s | `.venv/bin/python -m pytest test/hummingbot/core/data_type/test_order_book.py test/hummingbot/core/event/test_event_logger.py test/hummingbot/core/event/test_event_forwarder.py test/hummingbot/core/test_clock.py` |
| native315-tests | 0 | 4.17s | `.venv/bin/python -m pytest test/hummingbot/core/data_type/test_order_book.py test/hummingbot/core/test_clock.py` |
| observed-loop-ownership-focused-tests-2 | 1 | 53.47s | `.venv/bin/python -m pytest test/hummingbot/core/utils/test_trading_pair_fetcher.py test/hummingbot/data_feed/candles_feed/btc_markets_spot_candles test/test_isolated_asyncio_wrapper_test_case.py test/test_logger_mixin_for_test.py test/hummingbot/connector/derivative/bitmart_perpetual test/hummingbot/connector/derivative/evedex_perpetual --tb=short` |
| observed-loop-ownership-focused-tests-3 | 0 | 103.08s | `.venv/bin/python -m pytest test/hummingbot/core/utils/test_trading_pair_fetcher.py test/hummingbot/data_feed/candles_feed/btc_markets_spot_candles test/test_isolated_asyncio_wrapper_test_case.py test/test_logger_mixin_for_test.py test/hummingbot/connector/derivative/bitmart_perpetual test/hummingbot/connector/derivative/evedex_perpetual --tb=short` |
| observed-loop-ownership-focused-tests | 4 | 0.62s | `.venv/bin/python -m pytest test/hummingbot/core/utils/test_trading_pair_fetcher.py test/test_isolated_asyncio_wrapper_test_case.py test/hummingbot/logger test/hummingbot/data_feed/candles_feed/btc_markets_spot_candles test/hummingbot/connector/exchange/bitmart test/hummingbot/connector/exchange/evedex --tb=short` |
| override-sync | 1 | 2.16s | `uv sync --all-extras --python 3.14` |
| packaged-cli-help | 0 | 0.84s | `uv run --frozen --all-extras python -m hummingbot.cli.main --help` |
| pandas315-tests | 0 | 2.78s | `.venv/bin/python -m pytest test/hummingbot/core/utils/test_map_df_to_str.py` |
| protobuf-sync | 0 | 73.16s | `uv sync --all-extras --python 3.15.0` |
| hummingbot-published-wheel-cli-audit.log | 0 | unknowns | `/tmp/hummingbot-cli-wheel-audit315/bin/python -I -c import sys,hummingbot,importlib.metadata as m; print(hummingbot.__file__); print(sys.path); print([(x.name,x.value) for x in m.distribution("hummingbot").entry_points]); print({n:m.version(n) for n in ["typer","pandas","numpy"]})` |
| python315-build | 0 | 246.43s | `env TA_INCLUDE_PATH=/opt/homebrew/opt/ta-lib/include TA_LIBRARY_PATH=/opt/homebrew/opt/ta-lib/lib uv build --python 3.15` |
| python315-core | -11 | 23.89s | `.venv315/bin/python -m pytest test/hummingbot/core` |
| python315-probe | 0 | 0.13s | `uv sync --all-extras --python 3.15 --dry-run` |
| python315-sync-2 | 1 | 188.12s | `env UV_PROJECT_ENVIRONMENT=.venv315 TA_INCLUDE_PATH=/opt/homebrew/opt/ta-lib/include TA_LIBRARY_PATH=/opt/homebrew/opt/ta-lib/lib uv sync --all-extras --python 3.15` |
| python315-sync-3 | 0 | 275.58s | `env UV_PROJECT_ENVIRONMENT=.venv315 TA_INCLUDE_PATH=/opt/homebrew/opt/ta-lib/include TA_LIBRARY_PATH=/opt/homebrew/opt/ta-lib/lib uv sync --all-extras --python 3.15` |
| python315-sync | 1 | 50.88s | `env UV_PROJECT_ENVIRONMENT=.venv315 uv sync --all-extras --python 3.15` |
| python315-tests | 2 | 43.93s | `.venv315/bin/python -m pytest test` |
| remaining-api-focused-tests-2 | 1 | 34.26s | `.venv/bin/python -m pytest test/hummingbot/connector/exchange/ndax test/hummingbot/connector/exchange/foxbit/test_foxbit_user_stream_data_source.py test/hummingbot/connector/exchange/foxbit/test_foxbit_exchange.py --tb=short` |
| remaining-api-focused-tests | 1 | 53.74s | `.venv/bin/python -m pytest test/hummingbot/connector/exchange/ndax test/hummingbot/connector/exchange/foxbit/test_foxbit_user_stream_data_source.py test/hummingbot/connector/exchange/foxbit/test_foxbit_exchange.py test/hummingbot/connector/derivative/binance_perpetual/test_binance_perpetual_user_stream_data_source.py test/hummingbot/connector/derivative/aevo_perpetual/test_aevo_perpetual_api_user_stream_data_source.py test/hummingbot/data_feed/candles_feed/lighter_perpetual_candles test/hummingbot/data_feed/candles_feed/lighter_spot_candles test/hummingbot/client/command/test_config_command.py test/hummingbot/strategy/cross_exchange_market_making/test_cross_exchange_market_making.py --tb=short` |
| repaired-315-lock | 0 | 2.09s | `uv lock --upgrade` |
| repaired-315-sync | 0 | 112.07s | `uv sync --all-extras --frozen --python 3.15.0` |
| repaired-existing-cli-and-runner-tests | 0 | 2.91s | `uv run --frozen --all-extras python -m pytest test/hummingbot/cli test/hummingbot/client/test_runner.py --tb=short` |
| repaired-final-build | 0 | 270.27s | `uv build --python 3.15` |
| repaired-final-compile | 0 | 0.45s | `.venv/bin/python -m compileall -q src vendor controllers` |
| repaired-final-tests-2 | 1 | 8.1s | `.venv/bin/python -m pytest test/hummingbot/cli/test_update.py test/hummingbot/strategy/test_strategy_v2_base.py test/hummingbot/strategy/utils/trailing_indicators/test_historical_volatility.py test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_auth.py test/hummingbot/strategy_v2/backtesting/test_backtesting_engine_directional.py` |
| repaired-final-tests | 4 | 1.03s | `.venv/bin/python -m pytest test/hummingbot/cli/test_update.py test/hummingbot/strategy/test_strategy_v2_base.py test/hummingbot/strategy/utils/trailing_indicators/test_historical_volatility.py test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_auth.py test/hummingbot/strategy_v2/backtesting/test_backtesting_engine_directional.py test/hummingbot/core/utils/test_async_utils.py` |
| repaired-focused-tests-2 | 1 | 15.19s | `.venv/bin/python -m pytest test/hummingbot/cli/test_update.py test/hummingbot/strategy/test_strategy_v2_base.py test/hummingbot/strategy/utils/trailing_indicators/test_historical_volatility.py test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_auth.py test/hummingbot/strategy_v2/backtesting/test_backtesting_engine_directional.py` |
| repaired-focused-tests-3 | 0 | 11.99s | `.venv/bin/python -m pytest test/hummingbot/cli/test_update.py test/hummingbot/strategy/test_strategy_v2_base.py test/hummingbot/strategy/utils/trailing_indicators/test_historical_volatility.py test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_auth.py test/hummingbot/strategy_v2/backtesting/test_backtesting_engine_directional.py` |
| repaired-focused-tests | 1 | 11.59s | `.venv/bin/python -m pytest test/hummingbot/cli/test_update.py test/hummingbot/strategy/test_strategy_v2_base.py test/hummingbot/strategy/utils/trailing_indicators/test_historical_volatility.py test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_auth.py test/hummingbot/strategy_v2/backtesting/test_backtesting_engine_directional.py` |
| repaired-full-tests-2 | 1 | 753.85s | `.venv/bin/python -m pytest test --continue-on-collection-errors` |
| repaired-full-tests | 2 | 16.23s | `.venv/bin/python -m pytest test` |
| repaired-hbot-console-help | 0 | 0.61s | `uv run --frozen --all-extras hbot --help` |
| repaired-legacy-source-help | 1 | 0.14s | `uv run --frozen --all-extras python bin/hummingbot_quickstart.py --help` |
| repaired-quickstart-console-help | 1 | 2.91s | `uv run --frozen --all-extras hummingbot_quickstart --help` |
| repaired-source-tests | 1 | 18.87s | `.venv/bin/python -m pytest test/hummingbot/cli/test_update.py test/hummingbot/strategy/test_strategy_v2_base.py test/hummingbot/strategy/utils/trailing_indicators/test_historical_volatility.py test/hummingbot/connector/exchange/coinbase_advanced_trade/test_coinbase_advanced_trade_auth.py test/hummingbot/strategy_v2/backtesting/test_backtesting_engine_directional.py` |
| repaired-src-bootstrap-legacy-help | 1 | 2.35s | `uv run --frozen --all-extras python bin/hummingbot_quickstart.py --help` |
| repaired-sync-2 | 0 | 0.58s | `uv sync --all-extras --frozen --python 3.15 --reinstall-package aioresponses` |
| repaired-sync | 0 | 1.57s | `uv sync --all-extras --python 3.15 --reinstall-package aioresponses` |
| response-fixture-reinstall | 0 | 0.45s | `uv sync --all-extras --frozen --python 3.15.0 --reinstall-package aioresponses` |
| response-fixture-sync | 0 | 99.27s | `uv sync --all-extras --python 3.15.0` |
| response-reinstall-final | 0 | 0.45s | `uv sync --all-extras --frozen --python 3.15.0 --reinstall-package aioresponses` |
| response-supported-tests | 0 | 2.04s | `.venv/bin/python -m pytest test/hummingbot/core/utils/test_map_df_to_str.py test/hummingbot/data_feed/candles_feed/binance_spot_candles/test_binance_spot_candles.py` |
| response-wheel | 0 | 0.34s | `uv build --project vendor/aioresponses --wheel --out-dir dist/aioresponses` |
| resumed-final-existing-full-tests | 0 | 901.32s | `.venv/bin/python -m pytest test --continue-on-collection-errors --tb=short` |
| scoped-protobuf-focused-tests-2 | 1 | 47.92s | `.venv/bin/python -m pytest test/hummingbot/connector/derivative/injective_v2_perpetual test/hummingbot/connector/derivative/dydx_v4_perpetual --tb=short` |
| scoped-protobuf-focused-tests-3 | 1 | 49.64s | `.venv/bin/python -m pytest test/hummingbot/connector/derivative/injective_v2_perpetual test/hummingbot/connector/exchange/injective_v2 test/hummingbot/connector/derivative/dydx_v4_perpetual --tb=short` |
| scoped-protobuf-focused-tests | 2 | 4.4s | `.venv/bin/python -m pytest test/hummingbot/connector/derivative/injective_v2_perpetual test/hummingbot/connector/derivative/dydx_v4_perpetual --tb=short` |
| scoped-protobuf-lock | 0 | 1.69s | `uv lock --upgrade` |
| scoped-protobuf-refresh-2 | 0 | 1.33s | `uv sync --all-extras --dev --reinstall-package injective-py` |
| scoped-protobuf-refresh | 0 | 1.29s | `uv sync --all-extras --dev --reinstall-package injective-py` |
| scoped-protobuf-sync | 0 | 125.66s | `uv sync --all-extras --dev --reinstall-package injective-py` |
| scoped-schema-provenance-2 | 0 | 1.92s | `.venv/bin/python -c import ast,hashlib,io,pathlib,urllib.request,zipfile;url='https://files.pythonhosted.org/packages/d6/eb/0cfab54e116152ad021222c36e4d8067a6193c7735e54cfb64429511a26a/injective_py-1.16.2-py3-none-any.whl';data=urllib.request.urlopen(url).read();digest=hashlib.sha256(data).hexdigest();assert digest=='8aacf4e628cefb5091c701855ac64f0ec3e12b8c23bfe85b91d965edf9e2f9b3';z=zipfile.ZipFile(io.BytesIO(data));extract=lambda s:[ast.literal_eval(n.args[0]) for n in ast.walk(ast.parse(s)) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='AddSerializedFile'];pairs=[(n,pathlib.Path('vendor/injective-py/src')/n) for n in z.namelist() if n.startswith('pyinjective/') and n.endswith('_pb2.py')];assert len(pairs)==403;assert all(extract(z.read(n).decode())==extract(p.read_text()) for n,p in pairs);print('verified original wheel SHA256',digest,'and byte-identical serialized schemas for',len(pairs),'generated modules')` |
| scoped-schema-provenance | 0 | 0.79s | `.venv/bin/python -c import ast,hashlib,io,pathlib,urllib.request,zipfile;url='https://files.pythonhosted.org/packages/d6/eb/0cfab54e116152ad021222c36e4d8067a6193c7735e54cfb64429511a26a/injective_py-1.16.2-py3-none-any.whl';data=urllib.request.urlopen(url).read();digest=hashlib.sha256(data).hexdigest();assert digest=='8aacf4e628cefb5091c701855ac64f0ec3e12b8c23bfe85b91d965edf9e2f9b3';z=zipfile.ZipFile(io.BytesIO(data));extract=lambda s:[ast.literal_eval(n.args[0]) for n in ast.walk(ast.parse(s)) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='AddSerializedFile'];pairs=[(n,pathlib.Path('vendor/injective-py/src')/n) for n in z.namelist() if n.startswith('pyinjective/') and n.endswith('_pb2.py')];assert len(pairs)==403;assert all(extract(z.read(n).decode())==extract(p.read_text()) for n,p in pairs);print('verified original wheel SHA256',digest,'and byte-identical serialized schemas for',len(pairs),'generated modules')` |
| ssl-resource-focused-tests-2 | 1 | 84.72s | `.venv/bin/python -m pytest test/hummingbot/connector/derivative/gate_io_perpetual test/hummingbot/connector/derivative/grvt_perpetual test/hummingbot/connector/exchange/coinbase_advanced_trade test/hummingbot/connector/exchange/gemini --tb=short` |
| ssl-resource-focused-tests | 1 | 86.21s | `.venv/bin/python -m pytest test/hummingbot/connector/derivative/gate_io_perpetual test/hummingbot/connector/derivative/grvt_perpetual test/hummingbot/connector/exchange/coinbase_advanced_trade test/hummingbot/connector/exchange/gemini --tb=short` |
| strict-source-compile | 0 | 1.73s | `.venv/bin/python -W error -m compileall -q src controllers scripts vendor` |
| sync-3.13 | 1 | 1.7s | `uv sync --all-extras --python 3.13` |
| sync-3.14 | 1 | 2.6s | `uv sync --all-extras --python 3.14` |
| sync-3.15 | 1 | 8.78s | `uv sync --all-extras --python 3.15` |
| task-ownership-focused-tests-2 | 0 | 39.98s | `.venv/bin/python -m pytest test/hummingbot/data_feed/candles_feed/btc_markets_spot_candles test/test_isolated_asyncio_wrapper_test_case.py test/test_logger_mixin_for_test.py test/hummingbot/connector/derivative/bitmart_perpetual test/hummingbot/connector/derivative/evedex_perpetual --tb=short` |
| task-ownership-focused-tests | 1 | 40.84s | `.venv/bin/python -m pytest test/hummingbot/data_feed/candles_feed/btc_markets_spot_candles test/test_isolated_asyncio_wrapper_test_case.py test/test_logger_mixin_for_test.py test/hummingbot/connector/derivative/bitmart_perpetual test/hummingbot/connector/derivative/evedex_perpetual --tb=short` |
| tests-2 | 3 | 17.79s | `.venv/bin/python -m pytest test` |
| tests | 1 | 0.04s | `<workspace>/hummingbot/.venv/bin/python -m pytest test` |
| updated-full-tests | 1 | 160.22s | `.venv/bin/python -m pytest test --continue-on-collection-errors` |
| upstream-coincurve-sync | 0 | 147.35s | `uv sync --all-extras --python 3.14` |
