import os.path
import requests
import json


def get_access_token():
    """Get the ACCESS_TOKEN for the API service"""

    endpoint = "https://api.hashtagify.me/oauth/token"
    access_token = ""

    if os.path.isfile('api_token.txt'):
        file = open("api_token.txt", "r")
        for line in file:
            access_token = line.split(' ')[-1]
        file.close()
    else:
        print("Generate your access token to use the API service")
        client_id = input("Enter your consumer key: ")
        client_secret = input("Enter your consumer secret: ")
        payload = "grant_type=client_credentials&"f"client_id={client_id}&"f"client_secret={client_secret}"
        headers = {
            'cache-control': "no-cache",
            'content-type': "application/x-www-form-urlencoded"
        }

        response = requests.request("POST", endpoint, data=payload, headers=headers)

        access_token = json.loads(response.text)["access_token"]

        token_string = open("api_token.txt", "w+")
        token_string.write(f"This is your access token for the API service: {access_token}")

    print(f"Your access token for the API service is {access_token} and "
          f"you will find it also in the 'api_token.txt' file")

    return access_token


get_access_token()
