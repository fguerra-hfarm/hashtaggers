import os
import csv
import re


def use_post_csv(filename):
    """Reading, using and preparing a given .csv file for the API.

    Use case of a specific scraped posts dataset, which pre-processes
    the words used and gives in return the frequency of the most used
    unique hashtags (not counting possible semantic variations).
    """
    for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__)) + '/data/'):
        try:
            with open(root + "/" + filename, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                hashtag_list = []
                for row in csv_reader:
                    tweet = row[0]
                    # seeking only the hashtags present in the given Twitter posts dataset
                    match = re.findall(r"#(\w+)", tweet)
                    # creating a list of the hashtags present in the given Twitter posts dataset
                    for _ in match:
                        hashtag_list.append(_)
                return hashtag_list
        except FileNotFoundError:
            print("File '%s' not found " % filename + "in the requested directory " +
                  os.path.dirname(os.path.abspath(__file__)) + "/data/")
            pass
