# HASHTAGGERS :hash:

<p align="center">
    <img src="https://img.shields.io/static/v1?label=Version&message=1.0&color=blue" />
    <img src="https://img.shields.io/static/v1?label=Twitter&message=100%&color=green?style=flat-square&logo=twitter" />
</p>

Welcome to our repository! :wave:

<img src="https://i.ibb.co/3WmGM3f/Twitter-Logo-White-On-Blue.png" alt="Twitter-Logo-White-On-Blue" border="0" align="right" width="120" height="120">

With this program, developed with love and dedication, you will be able to:
1) Analyse a Twitter hashtag very deeply (API: [Hashtagify.me](https://hashtagify.me/));
    - Get your insights and stats from a proven working service;
2) Clean a dataset of posts and export from it, does not matter the social, all the hashtags that are present. :top: 

Since April 2011, hashtagify.me analysed over 8,785,728,584 tweets, collecting data about 12,412,341 hashtags!
Our goal is to provide the best tool to exploit, with the most advanced Twitter hashtag tracking tool on the market, a way to extrapolate insights regarding hashtags used on Twitter with the best accuracy!
We look for size and the reliability on the data, we want precision.

Our program will create a suit that can use the Hashtagify database in order to have access to all the information needed and bring also some additional functions.

## Usage

<details><summary><b>Show requirements</b></summary>

### Requirements

Since the program runs with **`python`** programming language you need to have it in your PC. [Here](https://www.python.org/downloads/) you can find the latest version for your OS, just press the download link and follow the installation guide!
     
Do not worry! Packages like: `argparse`, `tabulate`, `requests`, `datapackage` will be later installed automatically by following the *"Installation"* section.

</details>

### Installation

The first step to follow in order to use this project is to download the repository from [GitHub](https://github.com/fguerra-hfarm/hashtaggers). Just click on the green button **Code**, than **Download ZIP** as shown below.

<p align="center">
    <img src="https://i.ibb.co/NZ7H1jN/download.gif" alt="download" border="0" width=45% height=45%>
</p>

Once you have the repository on your local workspace, open the terminal in the repository directory and run the following command line: `$ python setup.py install`.  
This command will install all the necessary requirements (with the packages stated above) in order to run everything with full potential. 

You can now use the project! :sunglasses: 

### Run it! :computer:

To do that just write `$ python main.py -h` and the magic will begin. :fire:

> **IMPORTANT** 
You need to have an Hashtagify account, you may do a 7-days free trial, and more importantly, you need to generate your **consumer key** and **consumer secret** for the API.
_Do not worry!_ You can do this in your personal account settings in [here](https://hashtagify.me/users/edit). Just scroll down and simply create a new app, you will then find your personal consumer strings. Now copy and paste them when requested by running the command line above, everything is automated! EASY!! :wink:

This is what you will get (after generating, the first time, your personal token for the API stated in the "IMPORTANT" note): 

<p align="center">
    <img src="https://i.postimg.cc/m2xpzjgx/run.gif" alt="run" width=80% height=80%>
</p>

Now you have the print of the whole project which will show you all the capabilities and let you choose between different options based on what you will write in the console. 

#### Menu parameters

You can choose to go for three different choices with this program: :computer:
 1. `$ python main.py 1`: lets you choose the hashtag, just type in input the name, so you can analyse it fully in depth;
 2. `$ python main.py 2`: lets you read a given *.csv* dataset and with a simple table of the top 5 hashtag present in it, according to the *frequency value*, you can start querying insights of an hashtag of your choice (this table is just a reference, which can be useful for specific analysis scenarios);
 3. `$ python main.py 3`: will read a given *.csv* dataset, analyse it, and return an export in which there will be displayed all the hashtags present (taken only once) under the name `hashtags.csv`.

> **Dataset formatting:** the mandatory requirements for the .csv dataset are that it must be composed of a single column of posts and it is located in the directory `../hashtaggers-main/use_csv_package/data/dataset.csv`. You must rename it **dataset.csv**.

A sample file is provided! Hope you like motorbikes since it is about November posts from @DucatiMotor! :motorcycle:

These three command line parameter above mentioned can be associated with *optional arguments*, so that you can print just what you want from the full output shown below.

```
$ python main.py 1

Hashtag that you want to analyse: #pizza     

Running...

#pizza is 69% popular on Twitter, its most used variant is pizza with 72.8% of use, the top influencer is BT21_ 
with a reach of 783312912, it is mostly in English with a presence of 61.58% and its most related tag is salsa 
with a correlation value of 1.13.


The most correlated tags to pizza are: salsa, recipe, rt, dinner, foodie, love, beer, pasta, yummy, foodporn, food 


Statistics for:  pizza 

Popularity: 69%

TABLE OF VARIANTS
╒═══════════╤══════════════╕
│ Variant   │   % of total │
╞═══════════╪══════════════╡
│ pizza     │        72.8  │
├───────────┼──────────────┤
│ Pizza     │        24.25 │
├───────────┼──────────────┤
│ PIZZA     │         2.9  │
├───────────┼──────────────┤
│ PIzza     │         0.01 │
├───────────┼──────────────┤
│ piZza     │         0.01 │
├───────────┼──────────────┤
│ PizzA     │         0.01 │
╘═══════════╧══════════════╛

TABLE OF LANGUAGES
╒════════════╤══════════════╕
│ Language   │   % of total │
╞════════════╪══════════════╡
│ en         │        61.58 │
├────────────┼──────────────┤
│ es         │         8.21 │
├────────────┼──────────────┤
│ und        │         6.28 │
├────────────┼──────────────┤
│ it         │         4.47 │
├────────────┼──────────────┤
│ pt         │         2.43 │
├────────────┼──────────────┤
│ fr         │         1.52 │
╘════════════╧══════════════╛

TABLE OF TOP INFLUENCERS
╒═════════════════╤═══════════════╕
│ Influencer      │   Total reach │
╞═════════════════╪═══════════════╡
│ BT21_           │     783312912 │
├─────────────────┼───────────────┤
│ Michael5SOS     │     596418925 │
├─────────────────┼───────────────┤
│ frontpagestocks │     381440919 │
├─────────────────┼───────────────┤
│ aaronpaul_8     │     352649079 │
├─────────────────┼───────────────┤
│ shfly3424       │     190541728 │
├─────────────────┼───────────────┤
│ MariahCarey     │     177053940 │
├─────────────────┼───────────────┤
│ ShawnMendes     │     114850892 │
├─────────────────┼───────────────┤
│ Simonna         │      98831044 │
├─────────────────┼───────────────┤
│ JeffreeStar     │      68058967 │
├─────────────────┼───────────────┤
│ UniquePizzaSubs │      64137437 │
├─────────────────┼───────────────┤
│ RealJamesWoods  │      58277997 │
╘═════════════════╧═══════════════╛
```

##### Optional arguments

By adding particular features in the command line parameters listed above, it is possible to filter the analysis of the hashtags in a more detailed and focused way based on which feature we want;

The optional arguments are:
 1. `-v, --verbose`: displays the all hashtag information in discursive form with the *popularity*, first top *variant*, most used *language*, its *top influencer @* and *reach* and the most *related hashtag* with its *correlation value*;
 2. `-t, --tables`: through this function the program will print a set of tables containing all the values for the selected hashtag regarding its *variants*, *languages*, and *top influencers @s and reach*;
 3. `-c, --correlated`: This command will return the list of hashtags most related to our reference hashtag.


##### Usage examples
 
By combining *positional arguments* (1 or 2 or 3) and *optional arguments* (shown above) you can obtain different possible results with different combinations (if you do not select the optional one the machine will show you all the features shown in the print above)
Let's see the possible arrangements:
 1. `$ python main.py 1 -v` : if you want to know in discursive and understandable way the description of an hashtag of your choice and want to read it easily;
 2. `$ python main.py 2 -t` : if, after having the program analyse your dataset, you want to display the tables explained above of the picked hashtag (maybe chosen on the occurrence of hashtags present in your dataset);
 3. `$ python main.py 1 -c` : if you are interested in knowing which hashtags are the most related to the one you have chosen;
 4. `$ python main.py 3 -v` : will run with **no problems** and it will give you the requested export based on your dataset (of course you need to respect the dataset requirements).

***Hopefully everything is clear, good luck! :blush:***

<p style="text-align:center;" ><b>We are Hashtaggers! We are born to analyse hashtags!</b></p>

#### Team

- Filippo Guerra ([@fguerra-hfarm](https://github.com/fguerra-hfarm)): filippo.guerra@student.h-farm.com
- Leonardo Levisse ([@LeoLevisse](https://github.com/LeoLevisse)): leonardo.levisse@student.h-farm.com
- Nicola Mrvosevic  ([@nicolamrv](https://github.com/nicolamrv)): nicola.mrvosevic@student.h-farm.com
- Giorgio Vizzini ([@giorgiovizzini](https://github.com/giorgiovizzini)): giorgio.vizzini@student.h-farm.com
- Diego Vedova ([@VeDiego](https://github.com/VeDiego)): diego.vedova@student.h-farm.com

#### License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)