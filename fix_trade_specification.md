<div class="center">
<p align="center"><img src="https://user-images.githubusercontent.com/523933/49741959-91a1da00-fc65-11e8-911f-521331f87174.png" align="center" width="15%" height="15%"></p>
  <h1 align="center">Clear Street</h1>
  <p align="center">
  	<h2 align="center">
    	FIX Trade Specification
  	</h2>
	</p>
</div>

FIX trade specification details the tags and values along with description of values for each trade field for processing incoming trades from OMS clients. We currently utilizing FIX 4.2 format.

### FIX inbound trade specification

| Name             | FIX Tag | Allowable Values | Type       | Length | Allocation | Away       | Bilateral  | Exchange   | Trasfer    | Description                                 | Example           |
| ---------------- | ------- | ---------------- | ---------- | ------ | ---------- | ---------- | ---------- | ---------- | ---------- | ------------------------------------------- | ----------------- |
| `Execution Transaction Type` | `20` | `0` `1` | `Integer` | `1` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `0-New` `1-Cancel` | `0` |
| `Trade Type` | `9001` | `A` `B` `E` `T` `W` | `String` | `1` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `A-Allocation` `B-Bilateral` `E-Exchange` `T-Transfer` `W-Away` | `B` |
| `Account ID` | `1` |  | `Integer` | `6` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | Clear Street provided account id | `100000` |
| `Behalf Of Account ID` | `109` |  | `Integer` | `6` | `Optional` | `Optional` | `Optional` | `Optional` | `Optional` | Clear Street provided account ID if this trade is on behalf of another account | `100001` |
| `Branch Office` | `9003` |  | `String` |  | `Optional` | `Optional` | `Optional` | `Optional` | `Optional` | Branch office for this trade | `BRANCHOFFICE` |
| `Trade ID` | `17` |  | `String` |  | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | Unique Trade ID for this trade. Must be unique across days | `1234567890ABC` |
| `Cancel Trade ID` | `9009` |  | `String` |  | `Conditionally Mandatory` | `Conditionally Mandatory` | `Conditionally Mandatory` | `Conditionally Mandatory` | `Conditionally Mandatory` | Original trade ID to cancel; Required for all Cancel trades | `ABC12345` |
| `Trade Date` | `75` |  | `Integer` | `8` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | Trade Date in `YYYYMMDD` format | `20201102` |
| `Instrument Identifier Type` | `22` | `1` `2` `4` `8` | `Integer` | `1` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `1-CUSIP 2-SEDOL 4-ISIN 8-TICKER` | `8` |
| `Instrument Identifier` | `48` |  | `String` |  | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | Instrument Identifier based on tag 22 | `AAPL` |
| `Instrument Country` | `421` |  | `String` | `3` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | ISO 3166 alpha-3 country code where the instrument trades | `USA` |
| `Instrument Currency` | `15` |  | `String` | `3` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Price` | `31` |  | `Decimal` |  | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | The price of the trade | `120.12` |
| `Quantity` | `32` |  | `Decimal` |  | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | The quantity of the trade (supports fractional quantities) | `2` |
| `Registered Rep` | `9002` |  | `String` |  | `Optional` | `Optional` | `Optional` | `Optional` | `Optional` | Registered rep on this trade | `REGREP` |
| `Side` | `54` | `1` `2` `5` `6` | `Integer` | `1` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `1-Buy` `2-Sell` `5-Sell Short` `6-Sell Exempt` | `1` |
| `Position Type` | `77` | `C` `O` | `String` | `1` | `Optional` | `Optional` | `Optional` | `Optional` | `Optional` | `C-Close ` `O-Open` | `O` |
| `Settlement Currency` | `120` |  | `String` | `3` | `Optional` | `Optional` | `Optional` | `Optional` | `Optional` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Settlement Date Type` | `63` | `0` `7` | `Integer` | `1` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `0-Regular` `7-When_Issued` | `0` |
| `Settlement Date` | `64` |  | `Integer` | `8` | `Conditionally Mandatory` | `Conditionally Mandatory` | `Conditionally Mandatory` | `Conditionally Mandatory` | `Conditionally Mandatory` | Defaults to 99991231 for when issued trades and not required for when issued trades. Settlement date in `YYYYMMDD` format | `20201104` |
| `Solicited` | `325` | `F` `T` | `String` | `1` | `Optional` | `Optional` | `Optional` | `Optional` | `Optional` | `F-Solicited` `T-Not Solicited` | `T` |
| `Trade Execution Time` | `60` |  | `Integer` | `9` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | Timestamp of when the trade occurred in milliseconds since unix epoch | `174220664` |
| `Capacity` | `47` | `A` `M` `P` `R` | `String` | `1` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `Mandatory` | `A-Agency` `M-Mixed` `P-Principal` `R-Riskless Principal` | `P` |
| `Contra Clearing Number` | `440` |  | `Integer` | `4` | `Not Required` | `Mandatory` | `Mandatory` | `Not Required` | `Not Required` | Contra-party's clearing number | `9132` |
| `Contra MPID` | `375` |  | `String` | `4` | `Not Required` | `Mandatory` | `Mandatory` | `Not Required` | `Not Required` | Contra-party's MPID | `CLST` |
| `Executing MPID` | `76` |  | `String` | `4` | `Not Required` | `Mandatory` | `Mandatory` | `Mandatory` | `Not Required` | Executing party's MPID | `ANON` |
| `Contra Side Qualifier` | `9004` | `5` `6` | `Integer` |  | `Not Required` | `Not Required` | `Not Required` | `Not Required` | `Not Required` | `5-Sell Short` `6-Sell Exempt` | `5` |
| `MIC` | `30` |  | `String` | `4` | `Not Required` | `Optional` | `Optional` | `Mandatory` | `Not Required` | ISO 10383 Market Identifer Code for the exchange | `NYSE` |
| `Commission` | `12` |  | `Decimal` |  | `Optional` | `Optional` | `Optional` | `Optional` | `Optional` | Commission charged or paid | `0.12` |
| `Omit SEC Fee` | `9005` | `F` `T` | `String` | `1` | `Optional` | `Optional` | `Optional` | `Optional` | `Optional` | True if SEC fees should not be applied | `T` |
| `Omit TAF Fee` | `9006` | `F` `T` | `String` | `1` | `Optional` | `Optional` | `Optional` | `Optional` | `Optional` | True if TAF fees should not be applied | `T` |
| `Locate ID` | `9007` |  | `String` |  | `Not Required` | `Conditionally Mandatory` | `Conditionally Mandatory` | `Conditionally Mandatory` | `Not Required` | Locate ID obtained for a short sale; Required for Sell Short | `123456` |
| `Locate Source` | `9008` |  | `String` |  | `Not Required` | `Conditionally Mandatory` | `Conditionally Mandatory` | `Conditionally Mandatory` | `Not Required` | Firm supplying the locate (usually MPID); Required for Sell Short | `CLST` |
| `Order ID` | `37` |  | `String` |  | `Optional` | `Optional` | `Optional` | `Optional` | `Not Required` | Order ID to link all the executions in the average price account | `123456` |
| `NSCC Clearing` | `9010` | `agu` `contra` `corr` `corr_fees` `qsr` | `String` |  | `Not Required` | `Optional` | `Optional` | `Not Required` | `Not Required` | `agu` `contra` `corr` `corr_fees` `qsr` | `qsr` |
| `Target Account ID` | `79` |  | `Integer` | `6` | `Mandatory` | `Not Required` | `Not Required` | `Not Required` | `Mandatory` | Target account ID | `100001` |

### FIX outbound (response) specification

| Name             | FIX Tag | Allowable Values | Type       | Description                                 | Example           |
| ---------------- | ------- | ---------------- | ---------- | ------------------------------------------- | ----------------- |
| `Trade Details` |  |  |  | FIX message received from OMS |  |
| `Response` | `9011` |  | `String` | ACK or NACK with reason | `accepted` |
