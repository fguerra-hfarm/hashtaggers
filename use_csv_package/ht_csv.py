import os
import csv
import re


def generate_csv(filename):
    """Reading, using and preparing a new .csv file from another one.

    Function that reads a .csv file of a specific scraped Twitter posts
    dataset, pre-processes the words in it and gives in return a new .csv
    file of all the present hashtags.
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
                    for hashtag in match:
                        if hashtag not in hashtag_list:
                            hashtag_list.append(hashtag)
                            hashtag_list.sort()
                # generating a new .csv file from our previous list of hashtags
                with open(os.path.dirname(
                        os.path.abspath(__file__)) + '/data/hashtags.csv',
                          'w+', newline='') as export:
                    csv_writer = csv.writer(export)
                    for row in hashtag_list:
                        csv_writer.writerow(['#' + row])
                print("Great, your export has been generated successfully!"
                      "\nYou will find it at this directory: " +
                      os.path.dirname(os.path.abspath(__file__))
                      + '/data/hashtags.csv\n')
        except FileNotFoundError:
            print("File '%s' not found " % filename +
                  "in the requested directory " +
                  os.path.dirname(os.path.abspath(__file__)) + '/data/\n')
            pass
