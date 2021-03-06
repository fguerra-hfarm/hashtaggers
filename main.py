import sys
import argparse
import textwrap
from time import sleep
from tabulate import tabulate
from collections import Counter
from use_csv_package import ht_csv
from use_csv_package import posts_csv
from hashtagify_package import api_token
from hashtagify_package import api_hashtagify


def check_choice(choice):
    """Menu choice check for positional arguments that must be 1 or 2 or 3"""
    input_choice = int(choice)
    if input_choice < 0 or input_choice > 4:
        raise argparse.ArgumentTypeError(
            "\n\nNumber %s is an invalid choice, "
            "you must select between 1/2/3 to run the program!\n" % choice)
    return input_choice


def parse_arguments():
    """Parsing the input for the program.

    This function requires one positional argument which has three options
    and offers three optional arguments for other functionalities such as
    printing specific analytics or generating a new .csv file.
    """
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                           HASHTAGGERS ANALYTICS
----------------------------------------------------------------------------
    Service to extrapolate insights regarding hashtags used on Twitter!
    Provided under paid license of the Hashtagify API for best accuracy

   Choose between analysing any hashtag of your choice, the most frequent
hashtags from a given dataset or go for the .csv cleaning and creation tool.

Menu:
1 <- Hashtag of your choice
2 <- Specific .csv dataset with a set of hashtags (see guidelines)
3 <- Generate a .csv file of all the present hashtags inside you dataset
'''))
    parser.add_argument('menu', type=check_choice, choices=[1, 2, 3],
                        help='Menu selection choices (pick one number)',
                        action='store')
    parser.add_argument('-v', '--verbose',
                        help='Complete hashtag information in a '
                             'verbose format', action='store_true')
    parser.add_argument('-t', '--tables',
                        help='Specific tables of insights regarding '
                             'the selected hashtag', action='store_true')
    parser.add_argument('-c', '--correlated',
                        help='Specific correlated hashtags to the one '
                             'that has been selected', action='store_true')
    print()
    arguments = parser.parse_args()
    return arguments


try:
    # Token validity check
    api_token.check_token()
    # Parsing the arguments
    args = parse_arguments()

    # Hashtagify API use
    # --------------------------------
    # Simple chosen hashtag
    if args.menu == 1:
        input_ht = input("Hashtag that you want to analyze: #")
        sleep(0.5)
        print("\nRunning...")
        if args.verbose:
            api_hashtagify.get_insights(vot='v', hashtag=input_ht.lower())
            if args.tables:
                api_hashtagify.get_insights(vot='t',
                                            hashtag=input_ht.lower())
            elif args.correlated:
                api_hashtagify.get_insights(vot='c',
                                            hashtag=input_ht.lower())
        elif args.tables:
            api_hashtagify.get_insights(vot='t', hashtag=input_ht.lower())
            if args.verbose:
                api_hashtagify.get_insights(vot='v',
                                            hashtag=input_ht.lower())
            elif args.correlated:
                api_hashtagify.get_insights(vot='c',
                                            hashtag=input_ht.lower())
        elif args.correlated:
            api_hashtagify.get_insights(vot='c', hashtag=input_ht.lower())
            if args.verbose:
                api_hashtagify.get_insights(vot='v',
                                            hashtag=input_ht.lower())
            elif args.tables:
                api_hashtagify.get_insights(vot='t',
                                            hashtag=input_ht.lower())
        else:
            api_hashtagify.get_insights(hashtag=input_ht.lower())
    # --------------------------------
    # Hashtag pick with reference to the given dataset "Most common" table
    elif args.menu == 2:
        topx = Counter(posts_csv.use_post_csv(
            filename='dataset.csv'))
        print(tabulate(topx.most_common(5),
                       headers=['Hashtag - #', 'Occurrence'],
                       tablefmt='fancy_grid', numalign='center'))
        sleep(0.5)
        input_ht = input(f"\nFrom the given table, you may choose one of the "
                         f"most recurrent hashtags for a complete analysis: #")
        sleep(0.5)
        print("\nRunning...")
        if args.verbose:
            api_hashtagify.get_insights(vot='v', hashtag=input_ht.lower())
            if args.tables:
                api_hashtagify.get_insights(vot='t',
                                            hashtag=input_ht.lower())
            elif args.correlated:
                api_hashtagify.get_insights(vot='c',
                                            hashtag=input_ht.lower())
        elif args.tables:
            api_hashtagify.get_insights(vot='t', hashtag=input_ht.lower())
            if args.verbose:
                api_hashtagify.get_insights(vot='v',
                                            hashtag=input_ht.lower())
            elif args.correlated:
                api_hashtagify.get_insights(vot='c',
                                            hashtag=input_ht.lower())
        elif args.correlated:
            api_hashtagify.get_insights(vot='c', hashtag=input_ht.lower())
            if args.verbose:
                api_hashtagify.get_insights(vot='v',
                                            hashtag=input_ht.lower())
            elif args.tables:
                api_hashtagify.get_insights(vot='t',
                                            hashtag=input_ht.lower())
        else:
            api_hashtagify.get_insights(hashtag=input_ht.lower())
    # --------------------------------
    # Generation of a new .csv file of only hashtags
    elif args.menu == 3:
        ht_csv.generate_csv(filename='dataset.csv')

# Possible occurring errors in using the program
except ValueError:
    print("Something went wrong, please retry!")
    sys.exit()

except PermissionError:
    print("Close the .csv files before running the program!")

except ConnectionError:
    print("Bad getaway error, please check your connection!")
