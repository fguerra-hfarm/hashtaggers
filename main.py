import argparse
from time import sleep

from api_hashtagify import get_insights


def menu_select():
    print("\nHASHTAGIFY API SERVICE\n"
          "\nChoose between analysing the most frequent hashtags from a given dataset or any hashtag of your choice.")
    print("\nType:"
          "\n1 <- Specific dataset with a set of hashtags"
          "\n2 <- Hashtag of your choice")
    choice = 0
    while choice != '1' or choice != '2':
        choice = input("Selection: ")
        if choice == '1' or choice == '2':
            break
        else:
            print("Please, choose between available options")
    print("\nOPTION SELECTED\n")
    sleep(0.3)
    return choice


def extrapolate(analysis_type, hashtag):
    if analysis_type == 'dataset':
        return get_insights(hashtag)
    elif analysis_type == 'my_own':
        return get_insights(hashtag)


parser = argparse.ArgumentParser(description="Service to extrapolate insights on hashtag's that are used on Twitter")
parser.add_argument("analysis_choice", type=str, help="Preference of analysis (data origin)",
                    choices=['dataset', 'my_own'])
parser.add_argument("hashtag", type=str, help="Hashtag that you want to analyse")
args = parser.parse_args()

service = get_insights(args.hashtag)
print(service)
