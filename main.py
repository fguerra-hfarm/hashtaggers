import argparse

# from api_token import get_access_token
from api_hashtagify import get_insights


def extrapolate(analysis_type, hashtag):
    if analysis_type == 'dataset':
        return get_insights(hashtag)
    elif analysis_type == 'my_own':
        return get_insights(hashtag)


parser = argparse.ArgumentParser(description="Service to extrapolate hashtag's insights that are used on Twitter")
parser.add_argument("analysis_choice", type=str, help="Preference of analysis (data origin)",
                    choices=['dataset', 'my_own'])
parser.add_argument("hashtag", type=str, help="Hashtag that you want to analyse")
args = parser.parse_args()

service = get_insights(args.hashtag)
print(service)

# get_access_token()
# table = Counter(use_csv()).most_common(5)
# print(tabulate(table, headers=["Hashtag - #", "Occurrence"], tablefmt="fancy_grid", numalign="center"))
# print()
# time.sleep(1)
# get_insights(hashtag=input(f"From the given table, you may choose one of the most recurrent hashtags "
#                            f"for a complete analysis: "))
