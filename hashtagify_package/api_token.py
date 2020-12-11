import os
import json
import requests


def get_access_token():
    """Generate the ACCESS_TOKEN for the API service

    All the process is automated.
    Just get your client_id and client_secret from your hashtagify
    account settings to proceed.
    """

    endpoint = 'https://api.hashtagify.me/oauth/token'

    print("Generating your access token to use the API service")
    client_id = input("Enter your consumer key: ")
    client_secret = input("Enter your consumer secret: ")
    payload = "grant_type=client_credentials&"f"client_id={client_id}" \
              f"&"f"client_secret={client_secret}"
    headers = {
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request('POST', endpoint, data=payload,
                                headers=headers)
    access_token = json.loads(response.text)['access_token']

    # Writing a .txt file with the generated token for user reference
    token_string = open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'api_token.txt'), 'w+')
    token_string.write(f"This is your access token for the API service:"
                       f" {access_token}")
    print(f"\nYour access token for the API service is {access_token} and "
          f"you will find it also in the 'api_token.txt' file")
    return access_token


def read_access_token():
    """Use the ACCESS_TOKEN for the API service in the program functions"""
    access_token = ""
    file = open(os.path.dirname(os.path.abspath(__file__)) +
                '/api_token.txt', 'r')
    for line in file:
        access_token = line.split(' ')[-1]
    file.close()
    return access_token


def check_token():
    """Check the ACCESS_TOKEN validity

    The token, if not valid, which might occur with error 401 of the API,
    needs to be regenerated with the 'get_access_token' function. All the
    process is automated. Just get your client_id and client_secret to proceed.
    """
    if os.path.isfile(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'api_token.txt')):
        endpoint = "https://api.hashtagify.me/1.0/tag/"
        headers = {
            'authorization': "Bearer " + read_access_token(),
            'cache-control': "no-cache"
        }
        response = requests.get(endpoint + 'hashtag_test', headers=headers)
        if response.status_code == 401:
            print("There is a problem with the API service...\n"
                  "Error status code: ", response.status_code, "\n")
            print("Your token is not valid, please follow the instruction "
                  "below to generate a new one.\n")
            get_access_token()
            print("\nToken generated successfully!")
    else:
        print("\nYou first need to generate your token in order to being"
              " able to use the API service!\n")
        get_access_token()
        print("\nToken generated successfully!")
