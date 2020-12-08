import requests
import json
from time import sleep
from datapackage import Package
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


def check_langcode(languages_code):
    package = Package('https://datahub.io/core/language-codes/datapackage.json')

    # check language in database
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            for i in range(len(resource.read())):
                if resource.read()[i][0] == languages_code:
                    return resource.read()[i][1].lower()


def get_insights(hashtag):
    endpoint = "https://api.hashtagify.me/1.0/tag/"
    headers = {
        'authorization': "Bearer " + read_access_token(),
        'cache-control': "no-cache"
    }
    response = requests.get(endpoint + hashtag, headers=headers)

    if response.ok:
        print("\nRunning...")
        json_data = response.json()
        with open('hashtag_data.json', 'w+') as f:
            json.dump(json_data, f, indent=2)

            popularity = json_data[hashtag]['popularity']
            variants = json_data[hashtag]['variants']
            variants_word = [_[0] for _ in variants][0]
            variants_perc = [_[1] for _ in variants][0]
            languages = json_data[hashtag]['languages']
            languages_code = [_[0] for _ in languages][0]
            languages_perc = [_[1] for _ in languages][0]
            top_influencers = json_data[hashtag]['top_influencers']
            top_influencers_name = [_[0] for _ in top_influencers][0]
            top_influencers_reach = [_[1] for _ in top_influencers][0]
            related_tag = json_data[hashtag]['related_tags']['name']
            related_tag_corr = json_data[hashtag]['related_tags']['correlation']
            print()
            print(f"#%s has been found in the JSON data" % hashtag,
                  f"and it is {popularity}% popular on Twitter, its most used variant is {variants_word} "
                  f"with {variants_perc}% of use, the top influencer is {top_influencers_name} "
                  f"with a reach of {top_influencers_reach}, it is mostly in {check_langcode(languages_code)} "
                  f"with a presence of {languages_perc}% and its most related tag is {related_tag} "
                  f"with a correlation value of {related_tag_corr}.")
            print()
            print("Here the full JSON insights of", hashtag, ":", json_data[hashtag])
            print()
            correlated_tags = ([key for key in json_data.keys()][1:])
            print(f"The most correlated tags to %s are:" % hashtag, ', '.join(correlated_tags))
            print()
            print('\nStatistics for: ', json_data[hashtag]['name'], '\n')
            print(f"Popularity: {popularity}%")

            print('\nTABLE OF VARIANTS')
            table1 = variants
            headers = ['Variant', '% of total']
            print(tabulate(table1, headers, tablefmt="fancy_grid"))

            print('\nTABLE OF LANGUAGES')
            table2 = languages
            headers = ['Language', '% of total']
            print(tabulate(table2, headers, tablefmt="fancy_grid"))

            print('\nTABLE OF TOP INFLUENCERS')
            table3 = top_influencers
            headers = ['Influencer', 'Total reach']
            print(tabulate(table3, headers, tablefmt="fancy_grid"))

            # print('\nTABLE OF TOP RELATED TAGS')
            # table4 = [[correlated_tags][related_tag_corr]]
            # headers = ['Correlated Hashtag - #', 'Correlation value']
            # print(tabulate(table4, headers, tablefmt="fancy_grid"))
    else:
        elif response.status_code == 404:
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
    sleep(1)
    data = get_insights(hashtag=input(f"From the given table, you may choose one of the most "
                                      f"recurrent hashtags for a complete analysis: "))
