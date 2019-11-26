<div class="center">
<p align="center"><img src="https://user-images.githubusercontent.com/523933/49741959-91a1da00-fc65-11e8-911f-521331f87174.png" align="center" width="15%" height="15%"></p>
  <h1 align="center">Clear Street</h1>
  <p align="center">
  	<h2 align="center">
    	Order Management System (OMS)
  	</h2>
	</p>
</div>

Clear Street integrates with third party Order Management Systems to book and access open orders. Margin accounts traded on Clear Street have buying power dependent on positional and cash holdings. OMSs are provided with start of day information necessary, and the OMS tracks an account's open orders, cash, and positions in real time.

## Sterling, Das

* https://www.sterlingtradingtech.com/
* https://dastrader.com/

| Name                                | Description                                         |
| ----------------------------------- | --------------------------------------------------- |
| `Account`                           | Clear Street's Mapping of Account ID                |
| `Long Market Value`                 | Value of Long Positions                             |
| `Short Market Value`                | Value of Short Positions                            |
| `Trade Cash Balance`                | Cash Balance                                        |
| `Call Amount`                       | Total Amount of Margin Calls                        |
| `Yesterday Call Amount`             | Yesterday's Total Amount of Margin Calls            |
| `SMA Balance`                       | Excess Equity Amount used to Calculate Buying Power |
| `Multiplier`                        | Margin Multiplier depending on Account Type         |
| `Exchange Requirement`              | Minimum Cash Needed to Trade by Exchange            |
| `House Requirement`                 | Minimum Cash Needed to Trade Clear Street           |
| `Day Trader Buying Power`           | Buying Power                                        |
| `Day Trader Buying Power Yesterday` | Previous Day's Buying Power                         |
| `Equity`                            | Total Value of Account, Cash and Positions          |


## Redi

Clear Street also integrates with Redi; the start-of-day file contains information regarding instrument holdings.

* https://www.refinitiv.com/en/products/redi-execution-management/

| Name               | Description                                     |
| ------------------ | ----------------------------------------------- |
| `Account`          | Clear Street's Mapping of Account ID            |
| `Symbol`           | Equity Symbol                                   |
| `Symbology`        | Symbol used (e.g. `CUSIP`)                      |
| `Exchange `        | Exchange that Symbol is Traded On (e.g. `NYSE`) |
| `AccType`          | Account Type (e.g. `Margin`)                    |
| `Shares`           | Number of shares of Symbol                      |
| `Price`            | Per Share Price of Symbol                       |
| `Currency`         | Currency of Price (`USD`)                       |
| `Value`            | Value of Shares, Shares x Price                 |
| `Underlying`*      | Underlying Stock of Option                      |
| `Class`*           | Option Class Symbol                             |
| `Strike`*          | Option Strike Price                             |
| `Expiration Date`* | Option Expiration Date                          |
| `PutCall`*         | Option Put or Call                              |

\* Options are currently not supported
