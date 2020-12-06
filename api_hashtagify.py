import requests
import json
from collections import Counter
from tabulate import tabulate

from posts_csv import use_csv

api_url = "https://api.hashtagify.me/1.0/tag/"


def read_access_token():
    access_token = ""
    file = open("api_token.txt", "r")
    for line in file:
        access_token = line.split(' ')[-1]
    file.close()
    return access_token


def get_stats_test():
    hashtag = ""
    c = Counter(use_csv()).most_common(5)

    table = c
    # print(tabulate(table, headers=["Hashtag - #", "Occurrence"], tablefmt="fancy_grid", numalign="center"))

    # for i in c:
        # tags_list = tags_list + i[0] + " "
    # url = api_url + tags_list

    headers = {
        'authorization': "Bearer " + read_access_token(),
        'cache-control': "no-cache"
    }

    for i in c:
        hashtag = hashtag + i[0]
        url = api_url + hashtag
        print(url)

    response = requests.request("GET", url, headers=headers)
    # data = response.json()

    # print(data)
    # print(url)
    print(response.text)


get_stats_test()
