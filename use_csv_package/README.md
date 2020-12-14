## Use a dataset :open_file_folder:

This package will read, analyse and clean a given `.csv` file.

#### Requirements for the dataset
The mandatory requirements for the .csv dataset are that it must be composed of a single column of posts, you must rename it **dataset.csv**, and you must locate it in the directory `../hashtaggers-main/use_csv_package/data/dataset.csv`.

A sample file is provided! Hope you like motorbikes since it is about November posts from [@DucatiMotor](https://twitter.com/ducatimotor)! :motorcycle:

In this folder you can find the following list of modules:
1. `posts_csv.py`
2. `ht_csv.py`

The **first** module: will read through the dataset, extrapolate all the hashtag present and prepare a list of all those for the main usage;

The **second** module: is the same format as the first but in addition it provides an output file `hashtags.csv` of all the unique hashtags present in the dataset.