import requests


#TODO Update to production endpoint
UPLOAD_ID = '4d26735eeba55b882d7151e44439de49f54abe7915bade45eff49a59e952a23a'
URL = "https://api.clearstreet.io/v1/uploads/{}".format(UPLOAD_ID)

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': '<add authorization token here>'
}

def main():
    response = requests.get(url=URL, headers=headers)
    print(response.status_code, response.text)


if __name__ == "__main__":
    main()
