import argparse
import textwrap
from collections import Counter
from tabulate import tabulate
from time import sleep

from api_token import read_access_token, check_token_validity
from api_hashtagify import get_insights
from posts_csv import use_csv
from ht_csv import generate_csv


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


def check_choice(choice):
    choice = int(choice)
    if choice != '1' != '2':
        raise argparse.ArgumentTypeError("%s is an invalid choice, you must select 1 or 2" % choice)
    return choice


def print_type():
    if args.menu == '1':
        table = Counter(use_csv()).most_common(5)
        print(tabulate(table, headers=["Hashtag - #", "Occurrence"], tablefmt="fancy_grid", numalign="center"))
        print()
        sleep(0.5)
        get_insights(hashtag=input(f"From the given table, you may choose one of the most "
                                   f"recurrent hashtags for a complete analysis: #"))
    if args.verbose:
        print()
    elif args.tables:
        print()
    elif args.correlated:
        print()
    elif args.file:
        generate_csv()


# noinspection PyTypeChecker
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
                                        HASHTAGIFY API SERVICE
    -------------------------------------------------------------------------------------------------------
            Service to extrapolate insights about hashtags used on Twitter!
            
            Choose between analysing the most frequent hashtags from a given dataset or any hashtag of your choice.
            
            Menu:
            1 <- Specific dataset with a set of hashtags
            2 <- Hashtag of your choice
        '''))
# parser.add_argument("hashtag", type=str,
#                     help="Hashtag that you want to analyse (will give you all kinds of insights)")
parser.add_argument("menu", type=check_choice, help="Selection of analysis", choices=[1, 2])
parser.add_argument("-v", "--verbose", help="Complete hashtag information in a verbose format",
                    action="store_true")
parser.add_argument("-t", "--tables", help="Only specific tables of insights regarding the selected hashtag",
                    action="store_true")
parser.add_argument("-c", "--correlated", help="Only specific correlated hashtags to the one that has been selected",
                    action="store_true")
parser.add_argument("-f", "--file", help="Generate a clean .csv file of only hashtags from the raw dataset",
                    action="store_true")
args = parser.parse_args()

program = get_insights(args.hashtag)
