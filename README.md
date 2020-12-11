# Hashtaggers
## Università Ca' Foscari di Venezia & H-FARM
### Lab of Software Development Project Work

Twitter posts content analysis on the different # used. Developed by using the API service provided by [Hashtagify.me](https://hashtagify.me/).



## Project Description

The goal of the project is to extrapolate insights regarding hashtags used on Twitter!
We used Hashtagify API to obtain all the information about the hashtags.
Hashtagify API allows us to analyze different variables regarding each hashtag present in a database of over 12 million hashtags.
We chose Hashtagify because it is the best Twitter hashtags analysis tool on the Internet.
The size and the reliability of the Hashtagify finder were the main features that led us to our choice. 
The Hashtagify API allows us to create a link between our work environment and the Hashtagify database in order to have access to all the information we need.

## How to test our project
The first step to follow in order to try the project is to download the repository by the [GitHub website](https://github.com/fguerra-hfarm/hashtaggers). Just click on the green button **Code**, than **Download ZIP**.

![enter image description here](/Users/giorgiovizzini/Desktop/Schermata%202020-12-10%20alle%2017.24.48.png)

Once you have the repository on your local workspace, open the terminal in the repository directory and run the following code: `python setup.py install`.  
This command will install all the necessary requirements (like packages) in order to run the program. 

You can now run the project! :sunglasses: 
Just write `$ python main.py -h`. 
This is what you see: 

![enter image description here](/Users/giorgiovizzini/Desktop/Schermata%202020-12-10%20alle%2017.45.55.png)

Now you have the print of the whole project which let you choice between different options: 

 

## **Menu**

You can choose to analyze three three different kind of dataset, the mandatory requirement is that the datasets to be uploaded consist of a single column.
The three main codes are:
 1. `$ python main.py 1` lets you chose the hashtag, so you can analyze it in depth according to the different *optional arguments* that we are going to se later 
 2. `$ python main.py 2` lets you upload a given *CSV* dataset and analyze oll the Twitter posts of the dataset. The final output will show you a table of the top 5 hashtag present, according to the *frequency value*. This table is a reference, useful, later, to analyze a hashtag of your choice (as in the first case).
 3. `$ python main.py 3`lets you upload a given *CSV* dataset, the algorithm will read and analyze it, returning an output in which a new export will be displayed, consisting of all the hashtags present, taken only once.

These three codes mentioned above are associated with the *positional arguments*, so, once the argument has been selected, you can proceed with the combination of the optional arguments.
          

## **Optional arguments**

By adding particular features in the codes listed above, it is possible to make the analysis of the datasets and, in particular, of the hashtags more detailed and focused only on the given feature (s);
The optional arguments are:

 1. `-v` (verbose): This option displays all the hashtag information associated with the *popularity*, *variants*, *languages*, *top influncers*, *correlation* and *related hashtags* indices , in discursive form;
 2. `-t` (tables): through this function the algorithm will print a table containing all the index values for the selected hashtag;
 3. `-c` (correlated): This command will return the list of hashtags most related to our reference hashtag.


**In conclusion...** 
combining *positional arguments* and *optional arguments* you can obtain different result with different code lines, remember that if you do not select the optional topic the machine will show you all the features listed above and that this combination makes sense only in presence of *arguments 1* and *argument 2*
let's see the possible arrangements:
 1. `$ python main.py 1 -v` : if you want to know the values of the indices relating to a hashtag of your choice and want to read them in a discursive and understandable way;
 2. `$ python main.py 1 -t` : if you want to display the same indexes within a table;
 3. `$ python main.py 1 -c` : if you are interested in knowing which hashtags are most related to the one you have chosen;
 4. `$ python main.py 2 -v` : if, after having the machine analyze your dataset, you want to read about the indeces of your hashtags;
 5.  `$ python main.py 2 -v` : if, after having the machine analyze your dataset, you want to visualize the table of the indexes;
 6. `$ python main.py 2 -v` : if, after having the machine analyze your dataset, you want to know the hashtags most related to yours.

***Thanks for your attention, we hope that everything is clear, good luck! :blush:***

**We are Hashtaggers! We are born to analyze hashtags!**

# Team
- Filippo Guerra ([fguerra-hfarm](https://github.com/fguerra-hfarm))
   filippo.guerra@student.h-farm.com
- Leonardo Levisse ([LeoLevisse](https://github.com/LeoLevisse))
   leonardo.levisse@student.h-farm.com
- Nicola Mrvosevic  ([nicolamrv](https://github.com/nicolamrv))
   nicola.mrvosevic@student.h-farm.com
- Giorgio Vizzini ([giorgiovizzini](https://github.com/giorgiovizzini))
   giorgio.vizzini@student.h-farm.com
- Diego Vedova ([VeDiego](https://github.com/VeDiego))
   diego.vedova@student.h-farm.com
