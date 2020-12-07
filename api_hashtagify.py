import requests
import json
import time
from collections import Counter
from tabulate import tabulate

from posts_csv import use_csv


def read_access_token():
    access_token = ""
    file = open('api_token.txt', 'r')
    for line in file:
        access_token = line.split(' ')[-1]
    file.close()
    return access_token


def get_insights(hashtag):

    endpoint = "https://api.hashtagify.me/1.0/tag/"
    headers = {
        'authorization': "Bearer " + read_access_token(),
        'cache-control': "no-cache"
    }
    response = requests.get(endpoint + hashtag, headers=headers)

    if response.ok:
        json_data = response.json()
        with open('hashtag_data.json', 'w+') as f:
            json.dump(json_data, f, indent=2)
            if hashtag in json_data:
                popularity = json_data[hashtag]["popularity"]
                variants = json_data[hashtag]["variants"]
                languages = json_data[hashtag]["languages"]
                top_influencers = json_data[hashtag]["top_influencers"]
                print()
                print(f"#%s has been found in the JSON data" % hashtag, f"and it is {popularity} popular, "
                      f"it has these variants: {variants}, these top influencers: {top_influencers} "
                      f"and it is mostly used in these languages: {languages}")
                print()
                print("Here the full JSON insights of", hashtag, ":", json_data[hashtag])
            else:
                print("#%s has not been found in JSON data, please try another hashtag that is present" % hashtag)
    else:
        if response.status_code == 404:
            print("Status code: ", response.status_code)
            print("Hashtag not found, there isn't enough data yet for the requested hashtag.")
        elif response.status_code == 429:
            print("Status code: ", response.status_code)
            print("The daily or hourly quota has been exceeded.")
        raise Exception("There is an error...")


if __name__ == "__main__":
    table = Counter(use_csv()).most_common(5)
    print(tabulate(table, headers=["Hashtag - #", "Occurrence"], tablefmt="fancy_grid", numalign="center"))
    print()
    time.sleep(1)
    data = get_insights(hashtag=input(f"From the given table, choose an hashtag for a complete analysis: "))
