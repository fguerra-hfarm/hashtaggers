import os
import json
import requests
from tabulate import tabulate
from datapackage import Package
from hashtagify_package import api_token


def check_langcode(languages_code):
    package = Package('https://datahub.io/core/language-codes/'
                      'datapackage.json')

    # check language in database
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            for i in range(len(resource.read())):
                if resource.read()[i][0] == languages_code:
                    return resource.read()[i][1].lower()


def get_insights(hashtag, vot="base"):
    endpoint = "https://api.hashtagify.me/1.0/tag/"
    headers = {
        'authorization': "Bearer " + api_token.read_access_token(),
        'cache-control': "no-cache"
    }
    response = requests.get(endpoint + hashtag, headers=headers, timeout=(30, 30)) # Max 30 seconds to connect to server and max 30 seconds to wait on response

    if response.ok:
        print("\nRunning...")
        j_data = response.json()
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hashtag_data.json'), 'w+') as f:
            json.dump(j_data, f, indent=2)

            popularity = j_data[hashtag]['popularity']
            variants = j_data[hashtag]['variants']
            variants_word = [_[0] for _ in variants][0]
            variants_perc = [_[1] for _ in variants][0]
            languages = j_data[hashtag]['languages']
            languages_code = [_[0] for _ in languages][0]
            languages_perc = [_[1] for _ in languages][0]
            top_influencers = j_data[hashtag]['top_influencers']
            top_influencers_name = [_[0] for _ in top_influencers][0]
            top_influencers_reach = [_[1] for _ in top_influencers][0]
            related_tag = j_data[hashtag]['related_tags']['name']
            related_tag_corr = j_data[hashtag]['related_tags']['correlation']
            if vot == 'v' or vot == 'base':
                print(f"\n#%s" % hashtag, f"is {popularity}% popular on Twitter, "
                                          f"its most used variant is "
                                          f"{variants_word} with "
                                          f"{variants_perc}% of use, "
                                          f"the top influencer "
                                          f"is {top_influencers_name} "
                                          f"with a reach "
                                          f"of {top_influencers_reach}, "
                                          f"it is mostly "
                                          f"in {check_langcode(languages_code)} "
                                          f"with a presence "
                                          f"of {languages_perc}% "
                                          f"and its most related tag "
                                          f"is {related_tag} "
                                          f"with a correlation value "
                                          f"of {related_tag_corr}.\n")
            if vot == 'c' or vot == 'base':
                correlated_tags = ([key for key in j_data.keys()][1:])
                print(f"\nThe most correlated tags to %s are:"
                      % hashtag, ', '.join(correlated_tags))

            if vot == 't' or vot == 'base':
                print('\nStatistics for: ', j_data[hashtag]['name'], '\n')
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
    else:
        if response.status_code == 404:
            print("Status code: ", response.status_code)
            print("Hashtag not found, "
                  "there isn't enough data yet for the requested hashtag.")
        elif response.status_code == 429:
            print("Status code: ", response.status_code)
            print("The daily or hourly quota has been exceeded.")

        raise Exception("There is an error...")
