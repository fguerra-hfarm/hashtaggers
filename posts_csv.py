import requests
import json
import csv
import sys
from collections import Counter
import re
import string

def import_csv():
    ht_list = []
    with open('brexit.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            words = row[2].replace("\n", " ")
            words = words.replace("\xa0", " ")
            words = words.replace("https:", "")
            words = words.replace("http:", "")

            remove = string.punctuation
            remove = remove.replace("#", "")  # don't remove hashtags
            pattern = r"[{}]".format(remove)  # create the pattern

            re.sub(pattern, "", words)
            words = words.split(" ")

            for word in words:
                try:
                    if word[0] == "#":
                        if "." in word[-1] or "," in word[-1] or "/" in word[-1] or "|" in word[-1] or ";" in word[-1]:
                            word = word[:-1]
                        if word.lower() not in ht_list:
                            ht_list.append(word.lower())
                except:
                    pass

        #with open('hashtag_list.csv', 'x', newline='') as hashtag_list:
        #    wr = csv.writer(hashtag_list)
        #    for row in ht_list:
        #        wr.writerow([row])

        #print(ht_list)
        #print("The number of hashtags to analyze from the file is:", len(ht_list))
        return ht_list

def hashtag_count():
    ht_list = []
    with open('hashtag_list.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            words = row[0]
            words = words.split(" ")

            for word in words:
                try:
                    if word[0] == "#":
                        if "." in word[-1] or "," in word[-1] or "/" in word[-1] or "|" in word[-1] or ";" in word[-1]:
                            word = word[:-1]
                        if word.lower() not in ht_list:
                            ht_list.append(word.lower())
                except:
                    pass

        ht_list = ' '.join(ht_list)
        ht_list_new = re.findall(r'\w+', ht_list)

        print(ht_list_new)
        print("The number of hashtags to analyze from the file is:", len(ht_list_new))
        print(Counter(ht_list_new).most_common(6)[1:])
        return ht_list_new

import_csv()
hashtag_count()