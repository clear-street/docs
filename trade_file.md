<div class="center">
<p align="center"><img src="https://user-images.githubusercontent.com/523933/49741959-91a1da00-fc65-11e8-911f-521331f87174.png" align="center" width="15%" height="15%"></p>
  <h1 align="center">Clear Street</h1>
  <p align="center">
  	<h2 align="center">
    	Trade File
  	</h2>
	</p>
</div>

Clear Street's trade file is a CSV file that contains post-trade details. This file is used by Clear Street to manage the life-cycle of all post-trade trading activity.

## Format

The trade file should be a CSV file with `*.csv` extension. The first row of the file must be the "header" row where you specifiy column names. Column names are case-insenstive, but we recommend you always use lowercase. Column ordering does *not* matter; you can specify the columns in the order you prefer.

Each row in the file represents a single trade. Columns that are unrecognized or columns that might be conditionally unapplicable, are ignored. A trade has a `type` that dictates what columns apply to it. Columns that do not apply to a specific trade type are ignored. Therefore, you can provide all columns in your file, and selectively populate each column for a given row. 

### Columns

| Name       | Type  | Description | Example |
| -----------| ------|-------------|----------------------------------------- |
| `type` | `string` | Trade type, either `bilateral_trade`, `exchange_trade`, `allocation_trade`, or `transfer_trade` | `exchange_trade` |
| `timestamp`  | `integer` |  Timestamp of when the trade occurred in milliseconds since unix epoch | `1571408966810` |
| `client_trade_id` | `string` | Your unique ID for this trade. Must be unique across days | `T-50264430-bc41` 
| `date`        | `integer` | Trade date for the trade in `YYYYMMDD` format | `20200101` |
| `account_id` | `integer` | Clear Street provided account_id the trade should be booked to | `100023` |
| `quantity` | `numeric` | The quantity of the trade (supports fractional quantities) | `100` |
| `price` | `numeric` | The price of the trade | `100.01` |
| `behalf_of_entity_id` | `integer` | Clear Street provided entity_id if this trade is on behalf of another legal entity | `23` |
| `solicited` | `bool` | True if this trade was solicited, false otherwise | `false`
| `registered_rep` | `string` | The registered rep on this trade | `joe` |
| `instrument.identifier` | `string` | The identifier string, e.g. `AAPL` if `identifier_type` is `ticker` | `AAPL` |
| `instrument.identifier_type` | `string` | Identifier type, either `ticker`, `cusip`, `isin` or `sedol` | `ticker` |
| `instrument.country` | `string` | ISO 3166 alpha-3 country code where the instrument trades | `USA` |
| `instrument.currency` | `string` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `side.direction` | `string` | Either `buy` or `sell` | `buy` |
| `side.qualifier` | `string` | Either `short`, `open` or `close` | `short`
| `settlement.currency` | `string` | ISO 4217 alpha-3 currency code in which to settle this trade | `USD` |
| `settlement.date` | `string` | Explicit settlement date for irregular-way settlement in `YYYYMMDD` foramt | `20200101` |
| `capacity` | `string` | Either `principal`, `agency`, `mixed`, or `riskless_principal` | `mixed` |
| `contra_mpid` | `string` | Contra-party's MPID | `CLST` |
| `contra_dtc_num` | `string` | Contra-party's DTCC number | `9100` |
| `contra_side_qualifier` | `string` | Contra-party side qualifier, either `short`, `open`, or `close` | `short` |
| `is_when_issued` | `bool` | True if the trade should be considered as "when issued" | `false` |
| `exec_mpid` | `string` | MPID fo the executing party, if different than `contra_mpid` | `9192` |
| `fees.commission` | `string` | Commission charged or paid | `12.30` |
| `fees.omit_sec` | `bool` | True if SEC fees should not be applied | `false` |
| `fees.omit_taf` | `bool` | True if TAF fees should not be applied | `false` |
| `locate.id` | `string` | ID of the locate obtained for a short-sale | `A234` |
| `locate.source` | `string` | Identifies the firm supplying the locate (usually the MPID) | `Z322` |
| `target_account_id` | `string` | Clear Street provided account_id that is the contra to this trade | `100024` |
| `mic` | `string` | ISO 10383 Market Identifer Code for the exchange where this trade took place | `XNYS` |

### Exchange Trade

This trade represents a trade between a trading entity and an exchange. For example, trading firm XYX buys 100 shares of AAPL directly on Nasdaq.

| Column | Required? | Default | Notes |
| - | - | - | - |
| `type` | Yes |
| `timestamp` | Yes |
| `client_trade_id` | Yes |
| `date` | Yes |
| `account_id` | Yes |
| `quantity` | Yes |
| `price` | Yes |
| `behalf_of_entity_id` | No | `null` |
| `solicited` | No | `false` |
| `registered_rep` | No | `null` |
| `instrument.identifier` | Yes |
| `instrument.identifier_type` | Yes |
| `instrument.country` | Yes |
| `instrument.currency` | Yes |
| `side.direction` | Yes |
| `side.qualifier` | No | `null` |
| `settlement.currency` | No | `USD` |
| `settlement.date` | No | `null` |
| `capacity` | Yes |
| `mic` | Yes |
| `exec_mpid` | Yes |
| `is_when_issued` | No | `false` |
| `fees.commission` | No | `null` |
| `fees.omit_sec` | No | `false` |
| `fees.omit_taf` | No | `false` |
| `locate.id` | Conditional | `null` | Required if short-sale |
| `locate.source` | Conditional | `null` | Required if short-sale |


### Bilateral Trade

This trade represents a trade between two trading entities. For example, trading XYZ buys 100 share of AAPL from trading firm ABC.

| Column | Required? | Default | Notes |
| - | - | - | - |
| `type` | Yes |
| `timestamp` | Yes |
| `client_trade_id` | Yes |
| `date` | Yes |
| `account_id` | Yes |
| `quantity` | Yes |
| `price` | Yes |
| `behalf_of_entity_id` | No | `null` |
| `solicited` | No | `false` |
| `registered_rep` | No | `null` |
| `instrument.identifier` | Yes |
| `instrument.identifier_type` | Yes |
| `instrument.country` | Yes |
| `instrument.currency` | Yes |
| `side.direction` | Yes |
| `side.qualifier` | No | `null` |
| `settlement.currency` | No | `USD` |
| `settlement.date` | No | `null` |
| `capacity` | Yes |
| `contra_mpid` | Yes |
| `contra_dtc_num` | Yes |
| `is_when_issued` | No | `false` |
| `exec_mpid` | Yes |
| `fees.commission` | No | `null` |
| `fees.omit_sec` | No | `false` |
| `fees.omit_taf` | No | `false` |
| `locate.id` | Conditional | `null` | Required if short-sale |
| `locate.source` | Conditional | `null` | Required if short-sale |


### Allocation Trade

| Column | Required? | Default | Notes |
| - | - | - | - |
| `type` | Yes |
| `timestamp` | Yes |
| `client_trade_id` | Yes |
| `date` | Yes |
| `account_id` | Yes |
| `quantity` | Yes |
| `price` | Yes |
| `behalf_of_entity_id` | No | `null` |
| `solicited` | No | `false` |
| `registered_rep` | No | `null` |
| `instrument.identifier` | Yes |
| `instrument.identifier_type` | Yes |
| `instrument.country` | Yes |
| `instrument.currency` | Yes |
| `side.direction` | Yes |
| `side.qualifier` | No | `null` |
| `settlement.currency` | No | `USD` |
| `settlement.date` | No | `null` |
| `target_account_id` | Yes |
| `capacity` | Yes |
| `contra_side_qualifier` | Yes |
| `fees.commission` | No | `null` |
| `fees.omit_sec` | No | `false` |
| `fees.omit_taf` | No | `false` |

### Transfer Trade

blah blah

| Column | Required? | Default | Notes |
| - | - | - | - |
| `type` | Yes |
| `timestamp` | Yes |
| `client_trade_id` | Yes |
| `date` | Yes |
| `account_id` | Yes |
| `quantity` | Yes |
| `price` | Yes |
| `behalf_of_entity_id` | No | `null` |
| `solicited` | No | `false` |
| `registered_rep` | No | `null` |
| `instrument.identifier` | Yes |
| `instrument.identifier_type` | Yes |
| `instrument.country` | Yes |
| `instrument.currency` | Yes |
| `side.direction` | Yes |
| `side.qualifier` | No | `null` |
| `settlement.currency` | No | `USD` |
| `settlement.date` | No | `null` |
| `target_account_id` | Yes |
| `capacity` | Yes |
| `fees.commission` | No | `null` |
| `fees.omit_sec` | No | `false` |
| `fees.omit_taf` | No | `false` |

