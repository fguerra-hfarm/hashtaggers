## Hashtagify API and its code implementation :open_file_folder:

In this folder you can find the following list of modules:
1. `api_token.py`
2. `api_hashstagify.py`

The **first** module: generates, reads and controls the API token. The first run of the project, in order to generate the _token id_, there will be the need of the _consumer key_ and the _consumer secret_ (can be found in the settings of your hashtagify account). Those are requested as a simple input to generate the token.

The **second** module: makes the magic happen! It is where we find the calls to get the insights, processing of the data through a `.json` output and preparation of the various prints for the `main.py` module which runs everything together.

### How does the Hashtagify API work?

##### The process is very simple: 

A request is sent to the *Hashtagify server* and the server provides a response in a `.json` file format containing all the raw info regarding the queried hashtag.
The output is structured as follows:

 - ***Name***: the name of the hashtag,
 - ***Popularity***: How much a hashtag is used worlwide based on a scale from 0 to 100 (where 0 means that is rarely or never used, while 100 it is the most popular);
 - ***Variants***: the spelling or writing variants of the hashtag;
 - ***Languages***: The top languages used with the hashtag, starting from the most used, with the percentage of usage;
 - ***Top_influencers***: a list of the top influencers on Twitter for the hashtag, with the measured generated impressions;
 - ***Correlation***: the correlation with the searched hashtag;
 - ***Related_tags***:  the hashtags related to your search by correlation or by popularity.