import requests
from collections import Counter
from tabulate import tabulate
from posts_csv import use_csv

access_token = '456d04c7ad9ffba7a32a73fd4c7b9173a421bbaba76b'
API_url = "https://api.ritekit.com/v1/stats/multiple-hashtags?tags="


def get_stats():
    # getting the top 5 hashtags by frequency, with their occurrence, from the analyzed .csv
    tags_list = ""
    c = Counter(use_csv()).most_common(5)
    # Fancy way to best show the most present hashtags to the user, for visual reference
    table = c
    print(tabulate(table, headers=["Hashtag - #", "Occurrence"], tablefmt="fancy_grid", numalign="center"))

    for i in c:
        tags_list = tags_list + i[0] + "%2C"
    url = API_url + tags_list[:-3]

    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data=payload, params={'client_id': access_token})
    data = response.json()
    print(data)

    return data


get_stats()
