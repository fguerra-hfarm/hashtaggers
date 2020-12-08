import time
from collections import Counter
from tabulate import tabulate

from api_token import get_access_token
from api_hashtagify import get_insights
from posts_csv import use_csv

get_access_token()
table = Counter(use_csv()).most_common(5)
print(tabulate(table, headers=["Hashtag - #", "Occurrence"], tablefmt="fancy_grid", numalign="center"))
print()
time.sleep(1)
get_insights(hashtag=input(f"From the given table, you may choose one of the most recurrent hashtags "
                           f"for a complete analysis: "))
