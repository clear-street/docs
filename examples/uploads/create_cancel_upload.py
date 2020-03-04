import requests

# TODO Update to production endpoint
URL = "https://api.clearstreet.io/v1/uploads/cancel"
headers = {'Authorization': '<add authorization token here>'}
files = {'file': ('trades.csv', 'text/csv')}


def main():
    response = requests.post(url=URL, headers=headers, files=files)
    print(response.status_code, response.text)


if __name__ == "__main__":
    main()
