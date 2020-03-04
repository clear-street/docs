import requests


#TODO Update to production endpoint
URL = "https://api.clearstreet.io/v1/trades"

headers = {
    'Content-Type': 'application/json',
    'Authorization': '<add authorization token here>'
}

payload = [{
   "type": "exchange_trade",
   "timestamp": 1556544618,
   "client_trade_id": "042918-1",
   "date": 20190304,
   "account_id": 100016,
   "mic": "XNAS",
   "exec_mpid": "CSMM",
   "capacity": "principal",
   "quantity": "100",
   "price": "140.00",
   "instrument": {
       "identifier": "ATRA",
       "identifier_type": "ticker",
       "currency": "USD",
       "country": "USA"
   },
   "side": {
       "direction": "buy"
   }
}]


def main():
    response = requests.post(url=URL, headers=headers, json=payload)
    print(response.status_code, response.text)


if __name__ == "__main__":
    main()
