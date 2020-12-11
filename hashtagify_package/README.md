## ** HOW DOES THE API WORK**

The API allows us to create a link between our work environment and the Hashtagify database in order to have access to all the information we need.

The process is very simple: a request is sent to the *Hashtagify server* and the server provides a response in a *.json* file containing all the hashtag info structured as follows:

 - ***Name***: the name of the hastag,
 - ***Popularity***: How much a hastag is used worlwide based on a scale from 0 to 100 (where 0 is a hastag that is rarely or never used, while 100 is the most popular hastag),
 - ***Variants***: the spelling or writing variants of the hastag,
 - ***Languages***: The top languages used with the hastag, starting from the most used, with the percentage of usage,
 -  ***Top_influencers***: a list of the top influencers on Twitter for the hashtag, with the measured generated impressions,
 -  ***Correlation***: the correlation with the searched hashtag,
 - ***Related_tags***:  the hashtags related to your search by correlation or by popularity.

There are also two modules: the *token modul*e and the *api_hashstagify* module.

The token module generates, controls and reads the token, entering as input, the first time we run the project, the consumer's secret and the consumer's keys that can be found in the settings of your hashtagify account to generate it in order to use the api service and query some data.

The second module, the api_hashtagify, is where we find all the various prints and calls for the api. The module allows us to get all the insights of the hashtags and prepare the setup for the main project file.