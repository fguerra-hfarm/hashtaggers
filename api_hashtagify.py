import requests
import json
from collections import Counter
from tabulate import tabulate

from twposts_csv import use_csv

endpoint = "https://api.hashtagify.me/1.0/tag/"


def read_access_token():
    access_token = ""
    file = open("api_token.txt", "r")
    for line in file:
        access_token = line.split(' ')[-1]
    file.close()
    return access_token


def get_json():
    c = Counter(use_csv()).most_common(10)
    table = c
    print(tabulate(table, headers=["Hashtag - #", "Occurrence"], tablefmt="fancy_grid", numalign="center"))
    print()
    hashtag = input(f"From the given table, choose an hashtag for a complete analysis: ")
    print()

    headers = {
        'authorization': "Bearer " + read_access_token(),
        'cache-control': "no-cache"
    }
    response = requests.get(endpoint + hashtag, headers=headers)

    if response.ok:
        json_data = response.json()
        with open('hashtag_data.json', 'w') as f:
            json.dump(json_data, f, indent=2)
        return json_data
    else:
        if response.status_code == 404:
            print("Status code: ", response.status_code)
            print("Hashtag not found, there isn't enough data yet for the requested hashtag.")
        elif response.status_code == 429:
            print("Status code: ", response.status_code)
            print("The daily or hourly quota has been exceeded.")
        raise Exception("There is an error...")


def show_stats(data):
    print("Data: ", data)
    popularity = data["popularity"]
    variants = data["variants"]
    languages = data["languages"]
    top_influencers = data["top_influencers"]
    print(f"This hashtag is {popularity} popular, has these variants: {variants}, "
          f"with these top influencers: {top_influencers} and it is mostly used in these languages: {languages}")


if __name__ == "__main__":
    data = get_json()
    show_stats(data)
