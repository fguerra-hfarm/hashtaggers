import os
import csv
import re


def use_post_csv(filename):
    """Reading, using and preparing a given .csv file for the API.

    Use case: from a specific dataset of posts, could be from any social
    media, the words are analysed and all the present written hashtags
    are given in return.
    """
    for root, dirs, files in os.walk(
            os.path.dirname(os.path.abspath(__file__)) + '/data/'):
        try:
            with open(root + '/' + filename,
                      'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                hashtag_list = []
                for row in csv_reader:
                    tweet = row[0]
                    """
                    From the given Twitter posts dataset it is seeking only
                    the hashtags present and creating a list of those.
                    """
                    match = re.findall(r'#(\w+)', tweet)
                    for _ in match:
                        hashtag_list.append(_)
                return hashtag_list
        except FileNotFoundError:
            print("File '%s' not found " % filename +
                  "in the requested directory " +
                  os.path.dirname(os.path.abspath(__file__)) + '/data/\n')
            pass
