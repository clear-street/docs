<div class="center">
<p align="center"><img src="https://user-images.githubusercontent.com/523933/49741959-91a1da00-fc65-11e8-911f-521331f87174.png" align="center" width="15%" height="15%"></p>
  <h1 align="center">Clear Street</h1>
  <p align="center">
  	<h2 align="center">
    	Order Management System (OMS)
  	</h2>
	</p>
</div>

Clear Street works with third party OMS vendors to track open orders, cash, and positions in real time. Below is a list of fields Clear Street may provide to vendors at the start of day. Currently, Clear Street integrates with [sterling](https://www.sterlingtradingtech.com/), [das](https://dastrader.com/), and [redi](https://www.refinitiv.com/en/products/redi-execution-management/).


## Fields

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
