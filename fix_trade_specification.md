<div class="center">
<p align="center"><img src="assets/logo.png" align="center" width="20%" height="20%"></p>
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
<p>Clear Street expects every message sent to have a unique continuous sequence number as part of message with tag <b>34=</b>. If there are any gaps in sequence numbers, a sequence reset message will sent to OMS client with tag <b>34=4</b>.</p>
<p>All trade messages must have tag <b>35=8</b> indicating that each message is an execution report. Please note that we have added few custom tags starting with 9001 to allow clients to send specific information needed for trades to be processed at our end. These tags are listed as part of the inbound specification.</p>


### FIX inbound trade specification for Allocation Trade

This trade type is used to facilitate average-price workflows, i.e. averaging many trades for a customer and allocating it to them as a single trade.

| Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | FIX Tag | Allowable Values | Type | Length | Required? | Description | Example |
| - | - | - | - | - | - | - | - |
| `Execution Transaction Type` | `20` | `0` `1` | `Integer` | `1` | `R` | `0-New` `1-Cancel` | `0` |
| `Trade Type` | `9001` | `A` | `String` | `1` | `R` | `A-Allocation` | `A` |
| `Account ID` | `1` |  | `Integer` | `6` | `R` | Clear Street provided account id | `100000` |
| `Behalf Of Account ID` | `109` |  | `Integer` | `6` | `O` | Clear Street provided account ID if this trade is on behalf of another account | `100001` |
| `Branch Office` | `9003` |  | `String` |  | `O` | Branch office for this trade | `BRANCHOFFICE` |
| `Trade ID` | `17` |  | `String` |  | `R` | Unique Trade ID for this trade. Must be unique across days | `1234567890ABC` |
| `Cancel Trade ID` | `9009` |  | `String` |  | `CR` | Original trade ID to cancel; Required for all Cancel trades | `ABC12345` |
| `Trade Date` | `75` |  | `Integer` | `8` | `R` | Trade Date in `YYYYMMDD` format | `20201102` |
| `Instrument Identifier Type` | `22` | `1` `2` `4` `8` | `Integer` | `1` | `R` | `1-CUSIP 2-SEDOL 4-ISIN 8-TICKER` | `8` |
| `Instrument Identifier` | `48` |  | `String` |  | `R` | Instrument Identifier based on tag 22 | `AAPL` |
| `Instrument Country` | `421` |  | `String` | `3` | `R` | ISO 3166 alpha-3 country code where the instrument trades | `USA` |
| `Instrument Currency` | `15` |  | `String` | `3` | `R` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Price` | `31` |  | `Decimal` |  | `R` | The price of the trade | `120.12` |
| `Quantity` | `32` |  | `Decimal` |  | `R` | The quantity of the trade (supports fractional quantities) | `2` |
| `Registered Rep` | `9002` |  | `String` |  | `O` | Registered rep on this trade | `REGREP` |
| `Side` | `54` | `1` `2` `5` `6` | `Integer` | `1` | `R` | `1-Buy` `2-Sell` `5-Sell Short` `6-Sell Exempt` | `1` |
| `Position Type` | `77` | `C` `O` | `String` | `1` | `O` | `C-Close ` `O-Open` | `O` |
| `Settlement Currency` | `120` |  | `String` | `3` | `O` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Settlement Date Type` | `63` | `0` `7` | `Integer` | `1` | `R` | `0-Regular` `7-When_Issued` | `0` |
| `Settlement Date` | `64` |  | `Integer` | `8` | `CR` | Defaults to 99991231 for when issued trades and not required for when issued trades. Settlement date in `YYYYMMDD` format | `20201104` |
| `Solicited` | `325` | `F` `T` | `String` | `1` | `O` | `F-Solicited` `T-Not Solicited` | `T` |
| `Trade Execution Time` | `60` |  | `Integer` | `9` | `R` | Timestamp of when the trade occurred in milliseconds since unix epoch | `174220664` |
| `Capacity` | `47` | `A` `M` `P` `R` | `String` | `1` | `R` | `A-Agency` `M-Mixed` `P-Principal` `R-Riskless Principal` | `P` |
| `Contra Side Qualifier` | `9004` | `5` `6` | `Integer` |  | `CR` | `5-Sell Short` `6-Sell Exempt` | `5` |
| `Commission` | `12` |  | `Decimal` |  | `O` | Commission charged or paid | `0.12` |
| `Omit SEC Fee` | `9005` | `F` `T` | `String` | `1` | `O` | True if SEC fees should not be applied | `T` |
| `Omit TAF Fee` | `9006` | `F` `T` | `String` | `1` | `O` | True if TAF fees should not be applied | `T` |
| `Order ID` | `37` |  | `String` |  | `O` | Order ID to link all the executions in the average price account | `123456` |

### FIX inbound example message for Allocation Trade
`8=FIX.4.29=24535=849=OMS_CLIENT56=0000913234=12914352=20201021-21:42:3420=09001=A1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=A76=ABCD79=10001710=180`


### FIX inbound trade specification for Away Trade

This trade type represents a customer executing away from Clear Street LLC. For example, direct customer of CLST routes order for execution to Goldman.

| Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | FIX Tag | Allowable Values | Type | Length | Required? | Description | Example |
| - | - | - | - | - | - | - | - |
| `Execution Transaction Type` | `20` | `0` `1` | `Integer` | `1` | `R` | `0-New` `1-Cancel` | `0` |
| `Trade Type` | `9001` | `W` | `String` | `1` | `R` | `W-Away` | `W` |
| `Account ID` | `1` |  | `Integer` | `6` | `R` | Clear Street provided account id | `100000` |
| `Behalf Of Account ID` | `109` |  | `Integer` | `6` | `O` | Clear Street provided account ID if this trade is on behalf of another account | `100001` |
| `Branch Office` | `9003` |  | `String` |  | `O` | Branch office for this trade | `BRANCHOFFICE` |
| `Trade ID` | `17` |  | `String` |  | `R` | Unique Trade ID for this trade. Must be unique across days | `1234567890ABC` |
| `Cancel Trade ID` | `9009` |  | `String` |  | `CR` | Original trade ID to cancel; Required for all Cancel trades | `ABC12345` |
| `Trade Date` | `75` |  | `Integer` | `8` | `R` | Trade Date in `YYYYMMDD` format | `20201102` |
| `Instrument Identifier Type` | `22` | `1` `2` `4` `8` | `Integer` | `1` | `R` | `1-CUSIP 2-SEDOL 4-ISIN 8-TICKER` | `8` |
| `Instrument Identifier` | `48` |  | `String` |  | `R` | Instrument Identifier based on tag 22 | `AAPL` |
| `Instrument Country` | `421` |  | `String` | `3` | `R` | ISO 3166 alpha-3 country code where the instrument trades | `USA` |
| `Instrument Currency` | `15` |  | `String` | `3` | `R` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Price` | `31` |  | `Decimal` |  | `R` | The price of the trade | `120.12` |
| `Quantity` | `32` |  | `Decimal` |  | `R` | The quantity of the trade (supports fractional quantities) | `2` |
| `Registered Rep` | `9002` |  | `String` |  | `O` | Registered rep on this trade | `REGREP` |
| `Side` | `54` | `1` `2` `5` `6` | `Integer` | `1` | `R` | `1-Buy` `2-Sell` `5-Sell Short` `6-Sell Exempt` | `1` |
| `Position Type` | `77` | `C` `O` | `String` | `1` | `O` | `C-Close ` `O-Open` | `O` |
| `Settlement Currency` | `120` |  | `String` | `3` | `O` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Settlement Date Type` | `63` | `0` `7` | `Integer` | `1` | `R` | `0-Regular` `7-When_Issued` | `0` |
| `Settlement Date` | `64` |  | `Integer` | `8` | `CR` | Defaults to 99991231 for when issued trades and not required for when issued trades. Settlement date in `YYYYMMDD` format | `20201104` |
| `Solicited` | `325` | `F` `T` | `String` | `1` | `O` | `F-Solicited` `T-Not Solicited` | `T` |
| `Trade Execution Time` | `60` |  | `Integer` | `9` | `R` | Timestamp of when the trade occurred in milliseconds since unix epoch | `174220664` |
| `Capacity` | `47` | `A` `M` `P` `R` | `String` | `1` | `R` | `A-Agency` `M-Mixed` `P-Principal` `R-Riskless Principal` | `P` |
| `Contra Clearing Number` | `440` |  | `Integer` | `4` | `R` | Contra-party's clearing number | `9132` |
| `Contra MPID` | `375` |  | `String` | `4` | `R` | Contra-party's MPID | `CLST` |
| `Executing MPID` | `76` |  | `String` | `4` | `R` | Executing party's MPID | `ANON` |
| `Contra Side Qualifier` | `9004` | `5` `6` | `Integer` |  | `CR` | `5-Sell Short` `6-Sell Exempt` | `5` |
| `MIC` | `30` |  | `String` | `4` | `O` | ISO 10383 Market Identifer Code for the exchange | `NYSE` |
| `Commission` | `12` |  | `Decimal` |  | `O` | Commission charged or paid | `0.12` |
| `Omit SEC Fee` | `9005` | `F` `T` | `String` | `1` | `O` | True if SEC fees should not be applied | `T` |
| `Omit TAF Fee` | `9006` | `F` `T` | `String` | `1` | `O` | True if TAF fees should not be applied | `T` |
| `Locate ID` | `9007` |  | `String` |  | `CR` | Locate ID obtained for a short sale; Required for Sell Short | `123456` |
| `Locate Source` | `9008` |  | `String` |  | `CR` | Firm supplying the locate (usually MPID); Required for Sell Short | `CLST` |
| `Order ID` | `37` |  | `String` |  | `O` | Order ID to link all the executions in the average price account | `123456` |
| `NSCC Clearing` | `9010` | `agu` `contra` `corr` `corr_fees` `qsr` | `String` |  | `O` | `agu` `contra` `corr` `corr_fees` `qsr` | `qsr` |

### FIX inbound example message for Away Trade
`8=FIX.4.29=25335=849=OMS_CLIENT56=0000913234=12914552=20201021-21:42:3420=09001=W1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=M440=0295375=ABCD76=WXYZ10=180`


### FIX inbound trade specification for Bilateral Trade

This trade represents a trade between two trading entities. For example, trading firm XYZ buys 100 share of AAPL from trading firm ABC.

| Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | FIX Tag | Allowable Values | Type | Length | Required? | Description | Example |
| - | - | - | - | - | - | - | - |
| `Execution Transaction Type` | `20` | `0` `1` | `Integer` | `1` | `R` | `0-New` `1-Cancel` | `0` |
| `Trade Type` | `9001` | `B` | `String` | `1` | `R` | `B-Bilateral` | `B` |
| `Account ID` | `1` |  | `Integer` | `6` | `R` | Clear Street provided account id | `100000` |
| `Behalf Of Account ID` | `109` |  | `Integer` | `6` | `O` | Clear Street provided account ID if this trade is on behalf of another account | `100001` |
| `Branch Office` | `9003` |  | `String` |  | `O` | Branch office for this trade | `BRANCHOFFICE` |
| `Trade ID` | `17` |  | `String` |  | `R` | Unique Trade ID for this trade. Must be unique across days | `1234567890ABC` |
| `Cancel Trade ID` | `9009` |  | `String` |  | `CR` | Original trade ID to cancel; Required for all Cancel trades | `ABC12345` |
| `Trade Date` | `75` |  | `Integer` | `8` | `R` | Trade Date in `YYYYMMDD` format | `20201102` |
| `Instrument Identifier Type` | `22` | `1` `2` `4` `8` | `Integer` | `1` | `R` | `1-CUSIP 2-SEDOL 4-ISIN 8-TICKER` | `8` |
| `Instrument Identifier` | `48` |  | `String` |  | `R` | Instrument Identifier based on tag 22 | `AAPL` |
| `Instrument Country` | `421` |  | `String` | `3` | `R` | ISO 3166 alpha-3 country code where the instrument trades | `USA` |
| `Instrument Currency` | `15` |  | `String` | `3` | `R` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Price` | `31` |  | `Decimal` |  | `R` | The price of the trade | `120.12` |
| `Quantity` | `32` |  | `Decimal` |  | `R` | The quantity of the trade (supports fractional quantities) | `2` |
| `Registered Rep` | `9002` |  | `String` |  | `O` | Registered rep on this trade | `REGREP` |
| `Side` | `54` | `1` `2` `5` `6` | `Integer` | `1` | `R` | `1-Buy` `2-Sell` `5-Sell Short` `6-Sell Exempt` | `1` |
| `Position Type` | `77` | `C` `O` | `String` | `1` | `O` | `C-Close ` `O-Open` | `O` |
| `Settlement Currency` | `120` |  | `String` | `3` | `O` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Settlement Date Type` | `63` | `0` `7` | `Integer` | `1` | `R` | `0-Regular` `7-When_Issued` | `0` |
| `Settlement Date` | `64` |  | `Integer` | `8` | `CR` | Defaults to 99991231 for when issued trades and not required for when issued trades. Settlement date in `YYYYMMDD` format | `20201104` |
| `Solicited` | `325` | `F` `T` | `String` | `1` | `O` | `F-Solicited` `T-Not Solicited` | `T` |
| `Trade Execution Time` | `60` |  | `Integer` | `9` | `R` | Timestamp of when the trade occurred in milliseconds since unix epoch | `174220664` |
| `Capacity` | `47` | `A` `M` `P` `R` | `String` | `1` | `R` | `A-Agency` `M-Mixed` `P-Principal` `R-Riskless Principal` | `P` |
| `Contra Clearing Number` | `440` |  | `Integer` | `4` | `R` | Contra-party's clearing number | `9132` |
| `Contra MPID` | `375` |  | `String` | `4` | `R` | Contra-party's MPID | `CLST` |
| `Executing MPID` | `76` |  | `String` | `4` | `R` |Executing party's MPID | `ANON` |
| `Contra Side Qualifier` | `9004` | `5` `6` | `Integer` |  | `CR` | `5-Sell Short` `6-Sell Exempt` | `5` |
| `MIC` | `30` |  | `String` | `4` | `O` | ISO 10383 Market Identifer Code for the exchange | `NYSE` |
| `Commission` | `12` |  | `Decimal` |  | `O` | Commission charged or paid | `0.12` |
| `Omit SEC Fee` | `9005` | `F` `T` | `String` | `1` | `O` | True if SEC fees should not be applied | `T` |
| `Omit TAF Fee` | `9006` | `F` `T` | `String` | `1` | `O` | True if TAF fees should not be applied | `T` |
| `Locate ID` | `9007` |  | `String` |  | `CR` | Locate ID obtained for a short sale; Required for Sell Short | `123456` |
| `Locate Source` | `9008` |  | `String` |  | `CR` | Firm supplying the locate (usually MPID); Required for Sell Short | `CLST` |
| `Order ID` | `37` |  | `String` |  | `O` | Order ID to link all the executions in the average price account | `123456` |
| `NSCC Clearing` | `9010` | `agu` `contra` `corr` `corr_fees` `qsr` | `String` | `O` | `agu` `contra` `corr` `corr_fees` `qsr` | `qsr` |

### FIX inbound example message for Bilateral Trade
`8=FIX.4.29=25335=849=OMS_CLIENT56=0000913234=12914152=20201021-21:42:3420=09001=B1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=M440=0295375=ABCD76=WXYZ10=180`


### FIX inbound trade specification for Exchange Trade

This trade represents a trade between a trading entity and an exchange. For example, trading firm XYX buys 100 shares of AAPL directly on Nasdaq.

| Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | FIX Tag | Allowable Values | Type | Length | Required? | Description | Example |
| - | - | - | - | - | - | - | - |
| `Execution Transaction Type` | `20` | `0` `1` | `Integer` | `1` | `R` | `0-New` `1-Cancel` | `0` |
| `Trade Type` | `9001` | `E` | `String` | `1` | `R` | `E-Exchange` | `E` |
| `Account ID` | `1` |  | `Integer` | `6` | `R` | Clear Street provided account id | `100000` |
| `Behalf Of Account ID` | `109` |  | `Integer` | `6` | `O` | Clear Street provided account ID if this trade is on behalf of another account | `100001` |
| `Branch Office` | `9003` |  | `String` |  | `O` | Branch office for this trade | `BRANCHOFFICE` |
| `Trade ID` | `17` |  | `String` |  | `R` | Unique Trade ID for this trade. Must be unique across days | `1234567890ABC` |
| `Cancel Trade ID` | `9009` |  | `String` |  | `CR` | Original trade ID to cancel; Required for all Cancel trades | `ABC12345` |
| `Trade Date` | `75` |  | `Integer` | `8` | `R` | Trade Date in `YYYYMMDD` format | `20201102` |
| `Instrument Identifier Type` | `22` | `1` `2` `4` `8` | `Integer` | `1` | `R` | `1-CUSIP 2-SEDOL 4-ISIN 8-TICKER` | `8` |
| `Instrument Identifier` | `48` |  | `String` |  | `R` | Instrument Identifier based on tag 22 | `AAPL` |
| `Instrument Country` | `421` |  | `String` | `3` | `R` | ISO 3166 alpha-3 country code where the instrument trades | `USA` |
| `Instrument Currency` | `15` |  | `String` | `3` | `R` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Price` | `31` |  | `Decimal` |  | `R` | The price of the trade | `120.12` |
| `Quantity` | `32` |  | `Decimal` |  | `R` | The quantity of the trade (supports fractional quantities) | `2` |
| `Registered Rep` | `9002` |  | `String` |  | `O` | Registered rep on this trade | `REGREP` |
| `Side` | `54` | `1` `2` `5` `6` | `Integer` | `1` | `R` | `1-Buy` `2-Sell` `5-Sell Short` `6-Sell Exempt` | `1` |
| `Position Type` | `77` | `C` `O` | `String` | `1` | `O` | `C-Close ` `O-Open` | `O` |
| `Settlement Currency` | `120` |  | `String` | `3` | `O` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Settlement Date Type` | `63` | `0` `7` | `Integer` | `1` | `R` | `0-Regular` `7-When_Issued` | `0` |
| `Settlement Date` | `64` |  | `Integer` | `8` | `CR` | Defaults to 99991231 for when issued trades and not required for when issued trades. Settlement date in `YYYYMMDD` format | `20201104` |
| `Solicited` | `325` | `F` `T` | `String` | `1` | `O` | `F-Solicited` `T-Not Solicited` | `T` |
| `Trade Execution Time` | `60` |  | `Integer` | `9` | `R` | Timestamp of when the trade occurred in milliseconds since unix epoch | `174220664` |
| `Capacity` | `47` | `A` `M` `P` `R` | `String` | `1` | `R` | `A-Agency` `M-Mixed` `P-Principal` `R-Riskless Principal` | `P` |
| `Executing MPID` | `76` |  | `String` | `4` | `R` | Executing party's MPID | `ANON` |
| `Contra Side Qualifier` | `9004` | `5` `6` | `Integer` |  | `CR` | `5-Sell Short` `6-Sell Exempt` | `5` |
| `MIC` | `30` |  | `String` | `4` | `R` | ISO 10383 Market Identifer Code for the exchange | `NYSE` |
| `Commission` | `12` |  | `Decimal` |  | `O` | Commission charged or paid | `0.12` |
| `Omit SEC Fee` | `9005` | `F` `T` | `String` | `1` | `O` | True if SEC fees should not be applied | `T` |
| `Omit TAF Fee` | `9006` | `F` `T` | `String` | `1` | `O` | True if TAF fees should not be applied | `T` |
| `Locate ID` | `9007` |  | `String` |  | `CR` | Locate ID obtained for a short sale; Required for Sell Short | `123456` |
| `Locate Source` | `9008` |  | `String` |  | `CR` | Firm supplying the locate (usually MPID); Required for Sell Short | `CLST` |
| `Order ID` | `37` |  | `String` |  | `O` | Order ID to link all the executions in the average price account | `123456` |

### FIX inbound example message for Exchange Trade
`8=FIX.4.29=24335=849=OMS_CLIENT56=0000913234=12914452=20201021-21:42:3420=09001=E1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=R76=ABCD30=NYSE10=180`


### FIX inbound trade specification for Transfer Trade

This trade type is to facilitate trade movement between Clear Street internal accounts. For example, trade movement from a proprietary account to an average price account.

| Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | FIX Tag | Allowable Values | Type | Length | Required? | Description | Example |
| - | - | - | - | - | - | - | - |
| `Execution Transaction Type` | `20` | `0` `1` | `Integer` | `1` | `R` | `0-New` `1-Cancel` | `0` |
| `Trade Type` | `9001` | `T` | `String` | `1` | `R` | `T-Transfer` | `T` |
| `Account ID` | `1` |  | `Integer` | `6` | `R` | Clear Street provided account id | `100000` |
| `Behalf Of Account ID` | `109` |  | `Integer` | `6` | `O` | Clear Street provided account ID if this trade is on behalf of another account | `100001` |
| `Branch Office` | `9003` |  | `String` |  | `O` | Branch office for this trade | `BRANCHOFFICE` |
| `Trade ID` | `17` |  | `String` |  | `R` | Unique Trade ID for this trade. Must be unique across days | `1234567890ABC` |
| `Cancel Trade ID` | `9009` |  | `String` |  | `CR` | Original trade ID to cancel; Required for all Cancel trades | `ABC12345` |
| `Trade Date` | `75` |  | `Integer` | `8` | `R` | Trade Date in `YYYYMMDD` format | `20201102` |
| `Instrument Identifier Type` | `22` | `1` `2` `4` `8` | `Integer` | `1` | `R` | `1-CUSIP 2-SEDOL 4-ISIN 8-TICKER` | `8` |
| `Instrument Identifier` | `48` |  | `String` |  | `R` | Instrument Identifier based on tag 22 | `AAPL` |
| `Instrument Country` | `421` |  | `String` | `3` | `R` | ISO 3166 alpha-3 country code where the instrument trades | `USA` |
| `Instrument Currency` | `15` |  | `String` | `3` | `R` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Price` | `31` |  | `Decimal` |  | `R` | The price of the trade | `120.12` |
| `Quantity` | `32` |  | `Decimal` |  | `R` | The quantity of the trade (supports fractional quantities) | `2` |
| `Registered Rep` | `9002` |  | `String` |  | `O` | Registered rep on this trade | `REGREP` |
| `Side` | `54` | `1` `2` `5` `6` | `Integer` | `1` | `R` | `1-Buy` `2-Sell` `5-Sell Short` `6-Sell Exempt` | `1` |
| `Position Type` | `77` | `C` `O` | `String` | `1` | `O` | `C-Close ` `O-Open` | `O` |
| `Settlement Currency` | `120` |  | `String` | `3` | `O` | ISO 4217 alpha-3 currency code in which the instrument trades | `USD` |
| `Settlement Date Type` | `63` | `0` `7` | `Integer` | `1` | `R` | `0-Regular` `7-When_Issued` | `0` |
| `Settlement Date` | `64` |  | `Integer` | `8` | `CR` | Defaults to 99991231 for when issued trades and not required for when issued trades. Settlement date in `YYYYMMDD` format | `20201104` |
| `Solicited` | `325` | `F` `T` | `String` | `1` | `O` | `F-Solicited` `T-Not Solicited` | `T` |
| `Trade Execution Time` | `60` |  | `Integer` | `9` | `R` | Timestamp of when the trade occurred in milliseconds since unix epoch | `174220664` |
| `Capacity` | `47` | `A` `M` `P` `R` | `String` | `1` | `R` | `A-Agency` `M-Mixed` `P-Principal` `R-Riskless Principal` | `P` |
| `Contra Side Qualifier` | `9004` | `5` `6` | `Integer` |  | `CR` | `5-Sell Short` `6-Sell Exempt` | `5` |
| `Commission` | `12` |  | `Decimal` |  | `O` | Commission charged or paid | `0.12` |
| `Omit SEC Fee` | `9005` | `F` `T` | `String` | `1` | `O` | True if SEC fees should not be applied | `T` |
| `Omit TAF Fee` | `9006` | `F` `T` | `String` | `1` | `O` | True if TAF fees should not be applied | `T` |

### FIX inbound example message for Transfer Trade
`8=FIX.4.29=24535=849=OMS_CLIENT56=0000913234=12914252=20201021-21:42:3420=09001=T1=10007817=CLIENT_TRADE_ID75=2020102122=448=US70450Y1038421=USA15=USD31=000213.48000032=0000000298754=263=064=2020102360=155169025700547=P76=ABCD79=10001710=180`


### FIX outbound (response) specification

| Name             | FIX Tag | Allowable Values | Type       | Description                                 | Example           |
| ---------------- | ------- | ---------------- | ---------- | ------------------------------------------- | ----------------- |
| `Trade Details` |  |  |  | FIX message received from OMS |  |
| `Response` | `9011` |  | `String` | ACK or NACK with reason | `accepted` |

