# Hummingbot Workflows

## Order Lifecycle

Every order in Hummingbot passes through the `InFlightOrder` state machine, tracked by the `ClientOrderTracker` within each connector. The lifecycle begins when a strategy requests an order and ends when the exchange confirms completion or failure.

```mermaid
sequenceDiagram
    participant S as Strategy
    participant CB as ConnectorBase
    participant EPB as ExchangePyBase
    participant COT as ClientOrderTracker
    participant IFO as InFlightOrder
    participant API as Exchange API
    participant UST as UserStreamTracker
    participant PS as PubSub Events

    S->>CB: buy/sell_with_specific_market()
    CB->>EPB: _create_order()
    EPB->>IFO: Create InFlightOrder(PENDING_CREATE)
    EPB->>COT: start_tracking_order(order)
    EPB->>API: POST /order (REST)
    API-->>EPB: order_id response
    EPB->>IFO: update(exchange_order_id, OPEN)
    EPB->>PS: emit BuyOrderCreated / SellOrderCreated

    loop Status Polling + User Stream
        UST->>API: WebSocket user stream
        API-->>UST: Order/Trade updates
        UST->>COT: process_order_update(OrderUpdate)
        COT->>IFO: update state
    end

    alt Order Filled
        UST->>COT: process_trade_update(TradeUpdate)
        COT->>IFO: update(PARTIALLY_FILLED / FILLED)
        COT->>PS: emit OrderFilled
        IFO->>IFO: accumulate executed amounts
        COT->>PS: emit BuyOrderCompleted / SellOrderCompleted
        PS->>S: did_complete_buy/sell_order()
    else Order Cancelled
        S->>CB: cancel(trading_pair, order_id)
        CB->>API: DELETE /order
        COT->>IFO: update(CANCELED)
        COT->>PS: emit OrderCancelled
        PS->>S: did_cancel_order()
    else Order Failed
        API-->>EPB: error response
        COT->>IFO: update(FAILED)
        COT->>PS: emit OrderFailure
        PS->>S: did_fail_order()
    end
```

## Market Making Order Placement (Pure Market Making)

The Pure Market Making strategy places bid and ask orders symmetrically around a reference price. On each tick, it evaluates whether existing orders need refreshing.

```mermaid
flowchart TD
    START[Clock Tick] --> CHECK{Strategy<br/>Running?}
    CHECK -->|No| END[Skip]
    CHECK -->|Yes| READY{Connector<br/>Ready?}
    READY -->|No| END
    READY -->|Yes| REFRESH{Order Refresh<br/>Time Elapsed?}

    REFRESH -->|No| AGING{Orders<br/>Too Old?}
    AGING -->|No| END
    AGING -->|Yes| CANCEL_OLD[Cancel Aged Orders]
    CANCEL_OLD --> END

    REFRESH -->|Yes| CANCEL[Cancel All Active Orders]
    CANCEL --> PRICE[Get Reference Price<br/>mid/last/best_bid/best_ask]

    PRICE --> PROPOSAL[Create Proposal<br/>bid_price = price * 1-bid_spread<br/>ask_price = price * 1+ask_spread]

    PROPOSAL --> LEVELS{Multiple<br/>Order Levels?}
    LEVELS -->|Yes| MULTI[Generate Level Prices<br/>price +/- level * level_spread]
    LEVELS -->|No| SINGLE[Single bid + ask]

    MULTI --> SKEW
    SINGLE --> SKEW

    SKEW{Inventory<br/>Skew Enabled?}
    SKEW -->|Yes| ADJUST[Adjust Amounts<br/>by Inventory Ratio]
    SKEW -->|No| BUDGET

    ADJUST --> BUDGET[Budget Check<br/>BudgetChecker.adjust_candidates]

    BUDGET --> HANGING{Hanging Orders<br/>Enabled?}
    HANGING -->|Yes| FILTER[Filter Proposals<br/>Keep Hanging Orders]
    HANGING -->|No| PLACE

    FILTER --> PLACE[Place Orders<br/>buy/sell_with_specific_market]

    PLACE --> EMIT[Emit BuyOrderCreated<br/>SellOrderCreated Events]
    EMIT --> END
```

## Cross-Exchange Market Making (XEMM)

XEMM places maker orders on one exchange and immediately hedges fills with taker orders on another exchange. This captures the spread between venues.

```mermaid
sequenceDiagram
    participant CLK as Clock
    participant XEMM as CrossExchangeMM
    participant Maker as Maker Exchange
    participant Taker as Taker Exchange
    participant OB_M as Maker OrderBook
    participant OB_T as Taker OrderBook

    CLK->>XEMM: tick(timestamp)
    XEMM->>OB_T: Get taker mid price
    XEMM->>OB_M: Get maker order book

    Note over XEMM: Calculate maker price:<br/>taker_price * (1 + min_profitability)

    alt No Active Orders
        XEMM->>Maker: Place bid at taker_mid * (1 - spread)
        XEMM->>Maker: Place ask at taker_mid * (1 + spread)
    else Orders Need Adjustment
        XEMM->>Maker: Cancel stale orders
        XEMM->>Maker: Place adjusted orders
    end

    Note over XEMM: Wait for fill...

    Maker-->>XEMM: OrderFilled event (maker buy filled)
    XEMM->>XEMM: Calculate hedge amount
    XEMM->>OB_T: Check taker liquidity
    XEMM->>Taker: Place taker sell (hedge)
    Taker-->>XEMM: OrderCompleted

    Note over XEMM: Net profit =<br/>taker_sell - maker_buy - fees
```

## Order Book Tracking

Each connector maintains real-time order books through the `OrderBookTracker` and `OrderBookTrackerDataSource`.

```mermaid
flowchart TD
    subgraph DataSource["OrderBookTrackerDataSource"]
        REST[REST Snapshot<br/>GET /depth]
        WS[WebSocket Stream<br/>Diffs + Trades]
    end

    subgraph Tracker["OrderBookTracker"]
        QUEUE["Message Queues<br/>_order_book_snapshot_stream<br/>_order_book_diff_stream<br/>_order_book_trade_stream"]
        TASKS["Async Tasks<br/>_order_book_snapshot_router<br/>_order_book_diff_router<br/>_order_book_trade_router"]
        BOOKS["OrderBook Dict<br/>{trading_pair: OrderBook}"]
    end

    subgraph OrderBook["OrderBook"]
        BIDS["Bids (sorted desc)"]
        ASKS["Asks (sorted asc)"]
        SNAP_TS["Snapshot Timestamp"]
        APPLY["apply_snapshot()<br/>apply_diffs()<br/>apply_trade()"]
    end

    REST -->|Initial Snapshot| QUEUE
    WS -->|Continuous Diffs| QUEUE
    WS -->|Trade Events| QUEUE
    QUEUE --> TASKS
    TASKS --> BOOKS
    BOOKS --> OrderBook
    APPLY --> BIDS
    APPLY --> ASKS
```

## Balance and Inventory Management

The connector tracks two types of balances: total balances and available balances (accounting for in-flight orders).

```mermaid
flowchart TD
    subgraph ExchangeAPI["Exchange API"]
        BAL_API[Balance Endpoint]
        ORDER_API[Active Orders]
    end

    subgraph ConnectorBase["ConnectorBase"]
        TOTAL["_account_balances<br/>{asset: Decimal}"]
        AVAIL["_account_available_balances<br/>{asset: Decimal}"]
        REAL_TIME{"_real_time_balance_update?"}
        IFO_SNAP["_in_flight_orders_snapshot"]
    end

    subgraph BudgetChecker["BudgetChecker"]
        ADJ["adjust_candidates()"]
        LOCK["_locked_balances"]
        QUANTIZE["quantize_order_amount()"]
    end

    subgraph Strategy["Strategy"]
        PROPOSAL["Order Proposals"]
        ACTUAL["Adjusted Orders"]
    end

    BAL_API -->|Periodic Poll / WS| TOTAL
    BAL_API -->|Periodic Poll / WS| AVAIL

    REAL_TIME -->|Yes| AVAIL
    REAL_TIME -->|No| IFO_SNAP
    IFO_SNAP -->|Calculate| AVAIL

    PROPOSAL --> ADJ
    ADJ --> TOTAL
    ADJ --> AVAIL
    ADJ --> QUANTIZE
    QUANTIZE --> ACTUAL
```

## Gateway Integration Flow

For DEX trading, Hummingbot communicates with a separate Gateway server that handles blockchain interactions.

```mermaid
sequenceDiagram
    participant HB as Hummingbot
    participant GW as GatewayHttpClient
    participant GWS as Gateway Server (Node.js)
    participant DEX as DEX Protocol
    participant BC as Blockchain

    Note over HB,GWS: Connection Setup
    HB->>GW: Initialize with SSL certs
    GW->>GWS: GET /status (health check)
    GWS-->>GW: {status: "ok", chains: [...]}

    Note over HB,BC: Price Discovery
    HB->>GW: get_price(chain, network, connector, pair)
    GW->>GWS: GET /amm/price
    GWS->>DEX: Query pool prices
    DEX-->>GWS: Price quote
    GWS-->>GW: {price, gasEstimate, ...}

    Note over HB,BC: Trade Execution
    HB->>GW: amm_trade(chain, network, connector, pair, side, amount)
    GW->>GWS: POST /amm/trade
    GWS->>DEX: Build swap transaction
    GWS->>BC: Sign & submit transaction
    BC-->>GWS: Transaction hash
    GWS-->>GW: {txHash, gasUsed, ...}

    Note over HB,BC: Transaction Monitoring
    loop Poll for confirmation
        HB->>GW: get_transaction_status(chain, txHash)
        GW->>GWS: GET /chain/poll
        GWS->>BC: Check receipt
        BC-->>GWS: Receipt (pending/confirmed)
        GWS-->>GW: {confirmed, gasUsed, ...}
    end
```

## WebSocket Data Streaming

Modern connectors use a dual-stream WebSocket architecture: one for public market data and one for private user data.

```mermaid
flowchart LR
    subgraph Public["Public WebSocket"]
        PUB_WS["ws://exchange/stream"]
        OB_SNAP["Order Book Snapshot"]
        OB_DIFF["Order Book Diff"]
        TRADES["Trade Events"]
    end

    subgraph Private["Private WebSocket (Authenticated)"]
        PRIV_WS["ws://exchange/user"]
        BAL_UPD["Balance Updates"]
        ORD_UPD["Order Updates"]
        FILL_UPD["Fill Updates"]
    end

    subgraph WebAssistant["WebAssistantsFactory"]
        AUTH["AuthBase<br/>(API Key, Signature)"]
        REST_A["RESTAssistant"]
        WS_A["WSAssistant"]
        THROTTLE["AsyncThrottler<br/>(Rate Limits)"]
        PRE["PreProcessors"]
        POST["PostProcessors"]
    end

    subgraph Connector["ExchangePyBase"]
        OBT_DS["OrderBookTrackerDataSource"]
        UST_DS["UserStreamTrackerDataSource"]
        OBT2["OrderBookTracker"]
        UST2["UserStreamTracker"]
        COT2["ClientOrderTracker"]
    end

    PUB_WS --> WS_A
    PRIV_WS --> WS_A
    WS_A --> AUTH
    WS_A --> THROTTLE
    WS_A --> PRE
    WS_A --> POST

    OB_SNAP --> OBT_DS
    OB_DIFF --> OBT_DS
    TRADES --> OBT_DS
    OBT_DS --> OBT2

    BAL_UPD --> UST_DS
    ORD_UPD --> UST_DS
    FILL_UPD --> UST_DS
    UST_DS --> UST2
    UST2 --> COT2
```

## Event System and Handlers

The event system is the backbone of communication between connectors and strategies. Events flow upward from connectors through the PubSub system to strategy event listeners.

### Market Events

Events defined in `src/hummingbot/core/event/events.py`:

| Event | Code | Trigger |
|-------|------|---------|
| `ReceivedAsset` | 101 | Asset deposit received |
| `BuyOrderCompleted` | 102 | Buy order fully filled |
| `SellOrderCompleted` | 103 | Sell order fully filled |
| `OrderCancelled` | 106 | Order cancelled |
| `OrderFilled` | 107 | Order partially or fully filled |
| `OrderExpired` | 108 | Order expired |
| `OrderUpdate` | 109 | Order state change |
| `TradeUpdate` | 110 | New trade fill |
| `OrderFailure` | 198 | Order placement failed |
| `TransactionFailure` | 199 | Transaction failed |
| `BuyOrderCreated` | 200 | Buy order submitted |
| `SellOrderCreated` | 201 | Sell order submitted |
| `FundingPaymentCompleted` | 202 | Perpetual funding payment |

### Account Events

| Event | Code | Trigger |
|-------|------|---------|
| `PositionModeChangeSucceeded` | 400 | Position mode changed |
| `PositionModeChangeFailed` | 401 | Position mode change failed |
| `BalanceEvent` | 402 | Balance update |
| `PositionUpdate` | 403 | Position change |
| `MarginCall` | 404 | Margin call warning |
| `LiquidationEvent` | 405 | Position liquidated |

### Strategy Event Listeners (V1)

The `StrategyBase` class registers Cython event listeners for each market event. When an event fires, the corresponding `c_did_*` method is called:

```
BuyOrderCompleted  -> c_did_complete_buy_order(event)
SellOrderCompleted -> c_did_complete_sell_order(event)
OrderFilled        -> c_did_fill_order(event)
OrderCancelled     -> c_did_cancel_order(event)
OrderExpired       -> c_did_expire_order(event)
OrderFailure       -> c_did_fail_order(event)
FundingPayment     -> c_did_complete_funding_payment(event)
```

### V2 Executor Event Forwarding

V2 executors use `SourceInfoEventForwarder` to route events to handler methods:

```
BuyOrderCreated    -> process_order_created_event()
SellOrderCreated   -> process_order_created_event()
OrderFilled        -> process_order_filled_event()
BuyOrderCompleted  -> process_order_completed_event()
SellOrderCompleted -> process_order_completed_event()
OrderCancelled     -> process_order_canceled_event()
OrderFailure       -> process_order_failed_event()
```

### V2 Strategy Tick Flow

```mermaid
flowchart TD
    TICK[Clock Tick] --> SV2[StrategyV2Base.on_tick]
    SV2 --> CTRL_TICK["For each Controller:<br/>controller.on_tick()"]
    CTRL_TICK --> PROCESS["controller.update_processed_data()"]
    PROCESS --> PROPOSE["controller.determine_executor_actions()"]
    PROPOSE --> ACTIONS{"Actions?"}

    ACTIONS -->|CreateExecutorAction| CREATE[executor_orchestrator.create_executor]
    ACTIONS -->|StopExecutorAction| STOP[executor_orchestrator.stop_executor]
    ACTIONS -->|StoreExecutorAction| STORE[executor_orchestrator.store_executor]

    CREATE --> EXEC_LOOP["Executor.control_loop()<br/>(independent async loop)"]
    EXEC_LOOP --> PLACE["Place/manage orders"]
    PLACE --> EVENTS["Process fill/cancel events"]
    EVENTS --> STATUS{"Executor<br/>Status?"}
    STATUS -->|Running| EXEC_LOOP
    STATUS -->|Terminated| REPORT["Generate ExecutorInfo report"]
```

---
## See Also
- [README](README.md) — Project overview and quick start
- [Architecture](architecture.md) — System design and components
- [State Management](state-management.md) — State lifecycle and data models
- [Development](development.md) — Development guide and best practices
