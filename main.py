import argparse
import textwrap
from collections import Counter
from tabulate import tabulate
from time import sleep

from api_hashtagify import get_insights
from posts_csv import use_csv
from ht_csv import generate_csv


def check_choice(choice):
    input_choice = int(choice)
    if input_choice < 0 or input_choice > 3:
        raise argparse.ArgumentTypeError("%s is an invalid choice, you must select 1 or 2" % choice)
    return input_choice


# noinspection PyTypeChecker
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
                                                HASHTAGIFY API SERVICE
    --------------------------------------------------------------------------------------------------------------------
            Service to extrapolate insights about hashtags used on Twitter!
            
            Choose between analysing the most frequent hashtags from a given dataset or any hashtag of your choice.
            
            Menu:
            1 <- Specific dataset with a set of hashtags
            2 <- Hashtag of your choice
        '''))
parser.add_argument('menu', nargs='*', type=check_choice, choices=[1, 2], default=[1, 2],
                    help='Menu selection of the wanted analysis')
parser.add_argument('-v', '--verbose', help='Complete hashtag information in a verbose format',
                    action='store_true')
parser.add_argument('-t', '--tables', help='Only specific tables of insights regarding the selected hashtag',
                    action='store_true')
parser.add_argument('-c', '--correlated', help='Only specific correlated hashtags to the one that has been selected',
                    action='store_true')
parser.add_argument('-f', '--file', help='Extra generation of a clean .csv file of only hashtags from the raw dataset '
                                         '(if present in the data folder)',
                    action='store_true')
args = parser.parse_args()


# def print_type():
#     if args.menu == 1:
#         print()
#         table = Counter(use_csv()).most_common(5)
#         print(tabulate(table, headers=["Hashtag - #", "Occurrence"], tablefmt="fancy_grid", numalign="center"))
#         sleep(0.5)
#         get_insights(hashtag=input(f"\nFrom the given table, you may choose one of the most "
#                                    f"recurrent hashtags for a complete analysis: #"))
#     elif args.menu == 2:
#         get_insights(hashtag=input("\nHashtag that you want to analyze: #"))
#     # elif args.verbose:
#     #     print()
#     # elif args.tables:
#     #     print()
#     # elif args.correlated:
#     #     print()
#     # elif args.file:
#     #     generate_csv()
#
#     return get_insights
#
#
# print_type()


def print_type(menu):
    if menu == 1:
        print()
        table = Counter(use_csv()).most_common(5)
        print(tabulate(table, headers=["Hashtag - #", "Occurrence"], tablefmt="fancy_grid", numalign="center"))
        sleep(0.5)
        get_insights(hashtag=input(f"\nFrom the given table, you may choose one of the most "
                                   f"recurrent hashtags for a complete analysis: #"))
    elif menu == 2:
        get_insights(hashtag=input("\nHashtag that you want to analyze: #"))
    # elif args.verbose:
    #     print()
    # elif args.tables:
    #     print()
    # elif args.correlated:
    #     print()
    # elif args.file:
    #     generate_csv()

    return get_insights


print_type(menu=2)
