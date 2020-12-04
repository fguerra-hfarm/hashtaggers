import csv
import re
import string
from collections import Counter


def use_csv():
    """Reading, using and preparing a given .csv file for the API.

    Use case of a specific scraped posts dataset, which pre-processes
    the words used and gives in return the frequency of the most used
    unique hashtags (not counting possible semantic variations).
    """
    ht_list = []
    with open('brexit.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            #  fist pre-processing of the words present in the posts
            words = row[2].replace("\n", " ")
            words = words.replace("\xa0", " ")
            words = words.replace("https:", "")
            words = words.replace("http:", "")

            # removing punctuation and using a pattern to not remove the hashtag from the words
            re.sub(r"[{}]".format(string.punctuation.replace("#", "")), "", words)
            words = words.split(" ")

            # creating a list of all the present hashtags in the posts
            for word in words:
                # noinspection PyBroadException
                try:
                    if word[0] == '#':
                        # checking the end of the word for any possible left punctuation and remove it
                        if "." in word[-1] or "," in word[-1] or ";" in word[-1] or "|" in word[-1] \
                                or "/" in word[-1] or "!" in word[-1] or "?" in word[-1] or ":" in word[-1] \
                                or "'" in word[-1] or "(" in word[-1] or ")" in word[-1]:
                            word = word[:-1]
                        # checking for a possible double # at the start of the word
                        if "#" in word[1]:
                            word = word[-1:]
                        # adding the checked word to the list of hashtags
                        ht_list.append(word.lower())
                except:
                    pass

        # processing the list of all the present hashtags and preparing it for the Counter package
        ht_list = ' '.join(ht_list)
        ht_list_new = re.findall(r'\w+', ht_list)

        # Helpful code to pre-check your dataset (not necessary for the all package functioning)
        # Look at the first 20 hashtags in my list for a control, its length and
        # the top most common 5 by frequency from the list

        first_values = (ht_list_new[:20])
        list_length = "The number of hashtags to analyse from the file is:", len(ht_list_new)
        top5 = Counter(ht_list_new).most_common(5)  # Counter gives the top 5 hashtags by frequency from the list

        # print(list_length, top5)
        return ht_list_new
