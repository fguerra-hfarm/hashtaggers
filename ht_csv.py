import csv
import re
import string


def generate_csv():
    """
    Function that reads a .csv file of a specific scraped Twitter posts
    dataset, pre-processes the words used and gives in return a new file
    of all the present hashtags. Easy start for other use cases scenarios.
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
            re.sub(r"[{}]".format(
                string.punctuation.replace("#", "")), "", words)
            words = words.split(" ")

            for word in words:  # creating a list of all the present hashtags in the posts
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
                        # adding the checked word once to the list of hashtags
                        if word.lower() not in ht_list:
                            ht_list.append(word.lower())
                            ht_list.sort()  # sort it for manual reference convenience
                except:
                    pass

    # generating a new .csv file from our previous list of hashtags
    with open('hashtags.csv', 'w+', newline='') as hashtag_list:
        wr = csv.writer(hashtag_list)
        for row in ht_list:
            wr.writerow([row])
    return ht_list
