<div class="center">
<p align="center"><img src="assets/logo.png" align="center" width="20%" height="20%"></p>
  <h1 align="center">Clear Street</h1>
  <p align="center">
    <h2 align="center">
      Client Allocation File
    </h2>
  </p>
</div>

Clear Street's client allocation file is a CSV file that contains instructions on how Clear Street should allocate a customer's trades.  The current use case for this file is limited to when a customer has executed away and needs to match average priced block trades with their executing broker, while allocating those blocks into different lots across more than one account that they have at Clear Street.  

When Clear Street receives this file, an internal process will aggregate the allocations by `omni account id`, `trade date`, `settlement date`, `price`, `side direction`, `side qualifier`, `side position`, `instrument identifier`,  `exec mpid`, and `contra clearing number` to create an average priced block trade that will attempt to match against the executing broker.  The block will then be allocated as instructed on the file.  

In the case where a client executes away and the executing broker expects to settle the individual allocations (in lieu of a block trade), the client is expected to send an `Away Trade` using the [trade file spec](https://github.com/clear-street/docs/blob/master/trade_file.md).

The client allocation file should be a CSV file with `*.csv` (lowercase) extension. The first row of the file must be the "header" row where you specify column names.  Column names are case-insensitive, but we recommend you always use lowercase.  Column ordering does *not* matter; you can specify the columns in the order you prefer.

Each row in the file represents a single allocation.  Columns that are unrecognized, or columns that might be conditionally unapplicable, are ignored. 

The filename must begin with the string `clientallocation` so that it can be automatically ingested and properly aggregated.   As a matter of best practice, the filename should also indicate the source of the trades, the version number, and the date formatted as `yyyymmdd`.  Additionally, `_` is preferred to spaces in filenames.  A good example of a filename would be `clientallocation_abcfirm_1_20230309.csv`.

### Columns

| Name       | Type  | Required? | Default Value | Description | Example | 
| -----------| ------|-------------|----------------------------------------- |----------------------------------------- |----------------------------------------- |
| `omni_account_id` | `string` | Yes | | Clear Street provided omnibus account id to which the executing broker should allege | `196789` |
| `client_trade_id` | `string` | Yes | | Unique ID for this trade. Must be unique forever | `20230309trade1` |
| `date` | `integer` | Yes | | Trade date for the allocation in YYYYMMDD format | `20230309` |
| `exec_mpid` | `string` | Yes | | MPID of the executing broker | `CLST` |
| `side.direction` | `string` | Yes | | Either `buy` or `sell` (from the client’s perspective) | `buy` |
| `side.qualifier` | `string` | No| `null` | Set to `short` if customer short sale, otherwise not required | `short` |
| `side.position` | `string` | No| `null` | Required for options trades, indicates opening or closing transaction (valid values are `open` or `close`) | `open` |
| `instrument.identifier` | `string` | Yes | | The identifier string, e.g. `AAPL` if `identifier_type` is ticker | `AAPL` |
| `instrument.identifier_type` | `string` | Yes | | Identifier type, either `ticker`, `cusip`, `isin` or `sedol` | `ticker` |
| `instrument.country` | `string` | Yes* | | ISO 3166 alpha-3 country code where the instrument trades.  Always required unless `instrument.identifier_type` is `sedol` (will be ignored in this case) | `USA` |
| `instrument.currency` | `string` | Yes* | | ISO 4217 alpha-3 currency code in which the instrument trades.  Always required unless `instrument.identifier_type` is `sedol` (will be ignored in this case) | `USD` |
| `quantity` | `numeric` | Yes | | The quantity of the allocation | `1000` |
| `price` | `numeric` | Yes | | The price of the allocation | `150.35` |
| `fees.commission` | `string` | No | `0` | Total commission of the allocation | `100` |
| `fixed_income.accrued_interest` | `numeric` | No | `0` | For an allocation of fixed income securities, the portion of a future interest payment that the buyer must pay the seller | `50.75` |
| `fees.omit_sec` | `bool` | No| `false` | `true` if SEC fees should not be applied | `true` |
| `capacity` | `string` | Yes| | Either `principal`, `agency`, `mixed`, or `riskless_principal` | `agency` |
| `account_id` | `integer` | Yes| | Clear Street provided account id to which the trade should be allocated | `123456` |
| `solicited` | `bool` | No| `false` | `true` if this trade was solicited, `false` otherwise. Default to `false` if not provided | `false` |
| `timestamp` | `integer` | No| derived value | Timestamp of when the trade occurred in milliseconds since unix epoch. Will default to time of trade ingestion if not provided | `1678394397000` |
| `contra_clearing_num` | `string` | No| derived value | Contra-party's clearing number (DTCC for equities). If not supplied the value will be derived from an internal MPID to clearing number mapping | `9132` |
