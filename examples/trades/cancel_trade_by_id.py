import requests


#TODO Update to production endpoint
TRADE_ID = "01E2K1TN24D8AMV0D6RY58HQFB"
URL = "https://api.clearstreet.io/v1/trades/{}".format(TRADE_ID)

headers = {
    'Content-Type': 'application/json',
    'Authorization': '<add authorization token here>'
}

def main():
    response = requests.delete(url=URL, headers=headers)
    print(response.status_code, response.text)


if __name__ == "__main__":
    main()
