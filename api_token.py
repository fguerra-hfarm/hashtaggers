import requests
import json


def get_access_token():
    """Get the ACCESS_TOKEN for the API service"""

    endpoint = "https://api.hashtagify.me/oauth/token"

    print("Generating your access token to use the API service")
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


def read_access_token():
    access_token = ""
    file = open('api_token.txt', 'r')
    for line in file:
        access_token = line.split(' ')[-1]
    file.close()
    return access_token


def check_token_validity():
    endpoint = "https://api.hashtagify.me/1.0/tag/"
    headers = {
        'authorization': "Bearer " + read_access_token(),
        'cache-control': "no-cache"
    }
    response = requests.get(endpoint + 'hashtag_test', headers=headers)
    if response.status_code == 401:
        print("There is a problem with the API service...\n"
              "Error status code: ", response.status_code, "\n")
        print("Your token is not valid, please follow the instruction below to generate a new one.\n")
        get_access_token()
        print("\nToken generated successfully!\n")
