<div class="center">
<p align="center"><img src="https://user-images.githubusercontent.com/523933/49741959-91a1da00-fc65-11e8-911f-521331f87174.png" align="center" width="20%" height="20%"></p>
  <h1 align="center">Clear Street</h1>
  <p align="center">
  	<h2 align="center">
    	SFTP Access
  	</h2>
	</p>
</div>

Clear Street uses the SFTP protocol to facilitate document access between clients and Clear Street. The SFTP protocol provides a secure and fast way to browse large amount of documents in a manual or programmatic format.

## Connecting to the SFTP Server

To access the SFTP server, you will need a FTP client, such as [Cyberduck](https://cyberduck.io/), FileZilla, or even the `sftp` command. programmatic access to the SFTP server is also possible, and sample code is provided below.

In addition to this, you will need your SSH key-pair, consisting of both a public and private key. Your private key is your password, so ensure that it is stored securely. The public key is what you have shared with Clear Street, and is used to uniquely identify, and confirm who is connecting. Finally, you will need your Clear Street provided username.

### Connection Details

The following are the connection details to the SFTP server:

| Host            | [sftp://sftp.clearstreet.io](sftp://sftp.clearstreet.io)     |
| --------------- | ------------------------------------------------------------ |
| Port            | 22                                                           |
| Username        | Your Clear Street provided username                          |
| Password        | Blank - Your SSH Private Key is used for this                |
| SSH Private Key | The SSH private key you generated, this is the file usually without the `.pub` extension |

Follow the instructions of your chosen FTP client to connect to the SFTP server.

### Programmatic Access

If you wish to connect using a programmatic method, the following Python sample code should help:

```python
import pysftp

srv = pysftp.Connection(host="sftp.clearstreet.io", username="clearstreet", private_key="/Path/To/File")

print(srv.listdir())

srv.close()
```

Note: if you get key file type errors, such as when using a OpenSSH private key format, you may need to convert to the RSA format, which can be done through the following command:

```bash
ssh-keygen -p -f /Path/To/File -m pem
```



## Directory and File Structure

Once you have connected to the SFTP server, you will be dropped into your home directory. Within this directory, you have read and write access, however, note that Clear Street can remove/cleanup non-Clear Street files at any time. 

The directory structure is as follows:

```
home
  |- 2019
    |- 01
      |- monthly
      |- 01
      |- 02
      |- 03
      |- 04
        |- folder1
          |- file1
          |- file2
        |- folder2
          |- ...
      |- ...
    |- 02
      |- ...
  |- 2020
    |- ...
```

Directories are organized by date, in a `YYYY/MM/DD` format. At the lowest level - a single day - dropped files are placed in folders according to their usage. Files that are delivered on a monthly basis are placed in a `monthly` directory under the corresponding year and month - `YYYY/MM/monthly`. 



### Daily Content

On a daily basis, two sets of files are sent: activity details and trade confirmations.

#### Activity Details

Daily activity details are published in the `activity` folder under each day. There will be files published here *regardless of any activity*. Files in this directory have the following format:

```
{Date in YYYMMDD Format}_{Activity Type}_{SHA256 Hash of the data}.csv
```

For example:

```
20190207_journal_DEB9D6AE8E39E8008343B6A3E3E3819E28FF20CD7BE4827B1E8A0CC0EE803030.csv
```

The activity files that are currently published are:

- Journal Activity
- Trade Activity
- Position Activity
- Summary Information

These files are published in CSV format, so they are both machine and human readable.

##### Journal Activity

The Journal Activity file details all journal movements made across per account for a specific day. This could involve cash movements or position movements. A sample journal entry in this file is as follows:

| Date     | Org Name     | Entity Name              | Account ID | Account Name | Account Full Name | Instrument Name | Description | Cusip     | Isin         | Sedol   | Currency | Instrument Type | Segment | Memo                  | TD Quantity | TD Amount | SD Quantity | SD Amount |
| -------- | ------------ | ------------------------ | ---------- | ------------ | ----------------- | --------------- | ----------- | --------- | ------------ | ------- | -------- | --------------- | ------- | --------------------- | ----------- | --------- | ----------- | --------- |
| 20190207 | Clear Street | Clear Street FTP Trading | 00XX00     | clstftp      | Clear Street FTP  | AAPL            | Apple Inc.  | 037833100 | US0378331005 | 2046251 |          | Common Equity   | sl      | DLVR Journal for AAPL | 4000        | 0         | 4000        | 0         |

##### Trade Activity

The Trade Activity file details all trades made, across per account for a specific day. A sample trade entry in this file is as follows:

| Date     | Org Name     | Entity Name              | Account ID | Account Name | Account Full Name | Trade Client ID     | Trade ID                   | Action | Instrument Name | Description | Cusip     | Isin         | Sedol   | Currency | Instrument Type | Side | Trade Date | Settle Date | Quantity | Price  | Gross Amount | Fee Bill | Fee Commission | Fee Ftt | Fee Local Tax | Fee PtmLevy | Fee Sec | Fee Taf | Net Amount |
| -------- | ------------ | ------------------------ | ---------- | ------------ | ----------------- | ------------------- | -------------------------- | ------ | --------------- | ----------- | --------- | ------------ | ------- | -------- | --------------- | ---- | ---------- | ----------- | -------- | ------ | ------------ | -------- | -------------- | ------- | ------------- | ----------- | ------- | ------- | ---------- |
| 20190207 | Clear Street | Clear Street FTP Trading | 00XX00     | clstftp      | Clear Street FTP  | clstUniqueIDTrade01 | 01DN50D767DTQ44FNRB7M1MZ60 | insert | AAPL            | Apple Inc.  | 037833100 | US0378331005 | 2046251 | USD      | Common Equity   | Buy  | 20190207   | 20190209    | 2000     | 100.37 | 200740       | 0        | 60             | 0       | 0             | 0           | 1.58    | 1.25    | 200802.83  |

##### Position Activity

The Position Activity file details all positions across per account for a specific day. This could be held positions, or positions awaiting settlement. A sample position entry in this file is as follows:

| Org Name     | Entity Name              | Account ID | Account Name | Account Full Name | Instrument Name | Description | Cusip     | Isin         | Sedol   | Currency | Instrument Type | Previous TD Quantity | Today TD Quantity | Closing Price | TD Long Market Value | TD Short Market Value | Previous SD Quantity | Today SD Quantity | SD Long Market Value | SD Short Market Value |
| ------------ | ------------------------ | ---------- | ------------ | ----------------- | --------------- | ----------- | --------- | ------------ | ------- | -------- | --------------- | -------------------- | ----------------- | ------------- | -------------------- | --------------------- | -------------------- | ----------------- | -------------------- | --------------------- |
| Clear Street | Clear Street FTP Trading | 00XX00     | clstftp      | Clear Street FTP  | AAPL            | Apple Inc.  | 037833100 | US0378331005 | 2046251 | USD      | Common Equity   | 0                    | 2000              | 100.54        | 201080               | 0                     | 0                    | 4000              | 402160               | 0                     |

##### Summary Activity

The Summary Activity file details account value per account for a specific day. A sample summary entry in this file is as follows:

| Org Name     | Entity Name              | Account ID | Account Name | Account Full Name | Currency | TD Long Market Value | TD Short Market Value | TD Balance | SD Long Market Value | SD Short Market Value | SD Balance |
| ------------ | ------------------------ | ---------- | ------------ | ----------------- | -------- | -------------------- | --------------------- | ---------- | -------------------- | --------------------- | ---------- |
| Clear Street | Clear Street FTP Trading | 00XX00     | clstftp      | Clear Street FTP  | USD      | 21080                | 0                     | 20178.66   | 42160                | 0                     | -500.67    |

#### Trade Confirmations

Daily trade confirmations are delivered to the `confirms` directory under every day where trades were done. These confirms are in PDF human readable format and are not expected to be machine readable. There is a trade confirm generated per account for each day where trades were made. The file has the following naming convention:

```
{Date in YYYMMDD Format}_{Account ID}_confirm_{SHA256 Hash of the data}.csv
```

For example:

```
20190207_00XX00_confirm_DEB9D6AE8E39E8008343B6A3E3E3819E28FF20CD7BE4827B1E8A0CC0EE803030.csv
```

### Monthly Content

On a monthly basis, account statements are delivered to the `YYYY/MM/monthly` folder. These statements are in PDF human readable format and are not expected to be machine readable. There is a statement generated per account. The file has the following naming convention:

```
{Date in YYYMM Format}_{Account ID}_statement_{SHA256 Hash of the data}.csv
```

For example:

```
201902_00XX00_statement_DEB9D6AE8E39E8008343B6A3E3E3819E28FF20CD7BE4827B1E8A0CC0EE803030.csv
```


