<div class="center">
<p align="center"><img src="https://user-images.githubusercontent.com/523933/49741959-91a1da00-fc65-11e8-911f-521331f87174.png" align="center" width="15%" height="15%"></p>
  <h1 align="center">Clear Street</h1>
  <p align="center">
  	<h2 align="center">
    	FIX Trade Specification
  	</h2>
	</p>
</div>

FIX trade specification details the tags and values along with description of values for each trade field for processing incoming trades from OMS clients. Clear Street currently utilizes FIX 4.2 format.

### Configuring FIX Session
<p>A FIX session is defined as a unique combination of a BeginString (the FIX version number <b>4.2</b>), a SenderCompID (OMS Client ID as defined by Clear Street), and a TargetCompID (Clear Street's ID <b>CLST</b>). A SessionQualifier can also be used to disambiguate otherwise identical sessions.</p>

<p>A FIX session has an active time period during which all data is transmitted. Clear Street currently accepts connections between 5 AM EST to 9 PM EST on all business days.</p>
<p>A Logon message (Tag <b>35=A</b>) must be sent to Clear Street on every business day to indicate the begining of activity and a Logout message (Tag <b>35=5</b>)must be sent to Clear Street indicating end of activity for that day.</p> 
<p>Clear Street also recommends exchange of heartbeats every 30 seconds by seding a message with tag <b>35=0</b>.</p>
<p>Clear Street execpts every message sent to have a unique continuous sequence number as part of message with tag <b>34=</b>. If there are any gaps in sequence numbers, a sequence reset message will sent to OMS client with tag <b>34=4</b>.</p>
<p>All trade messages must have tag <b>35=8</b> indicating that each message is an execution report. Please note that we have added few custom tags starting with 9001 to allow clients to send specific information needed for trades to be processed at our end. These tags are listed as part of the inbound specification.</p>

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

### FIX inbound example message for Bilateral trade
`8=FIX.4.29=25335=849=OMS_CLIENT56=0000913234=12914152=20201021-21:42:3420=09001=B1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=M440=0295375=ABCD76=WXYZ10=180`

### FIX inbound example message for Transfer trade
`8=FIX.4.29=24535=849=OMS_CLIENT56=0000913234=12914252=20201021-21:42:3420=09001=T1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=P76=ABCD79=10001710=180`

### FIX inbound example message for Allocation trade
`8=FIX.4.29=24535=849=OMS_CLIENT56=0000913234=12914352=20201021-21:42:3420=09001=A1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=A76=ABCD79=10001710=180`

### FIX inbound example message for Exchange trade
`8=FIX.4.29=24335=849=OMS_CLIENT56=0000913234=12914452=20201021-21:42:3420=09001=E1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=R76=ABCD30=NYSE10=180`

### FIX inbound example message for Away trade
`8=FIX.4.29=25335=849=OMS_CLIENT56=0000913234=12914552=20201021-21:42:3420=09001=W1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=M440=0295375=ABCD76=WXYZ10=180`
