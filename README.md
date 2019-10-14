# Python-Challenge
## Introduction
* This repo contains two python scripts that summarizes data and exports the summary to the terminal and `.csv` files.

## Summarizing Banking Data
* Files can be found in the `PyBank` folder
  * `main.py` = python script
  * `budget_data.csv` = original data
  * `budget_data_summary.csv` = summarized data created from the python script

* Taking a file containing months with their corresponding profits/losses, `main.py` summarizes the data. The results are printed to the terminal and a `.csv` file in the same directory as the script:
  * Total months in the dataset
  * Net total profits
  * Average change in profits
  * Greatest increase in profits
  * Greatest decrease in profits
  
* Note that the headers are not required, but the dates must be in the first column and the profit/losses in the second column:

![budget_data](https://github.com/L0per/Python-Challenge/blob/master/Images/budget_data.JPG?raw=true)

* The data is summarized in the terminal and `.csv` file as shown below:

!![budget_data_summary](https://github.com/L0per/Python-Challenge/blob/master/Images/budget_summary.JPG?raw=true)

## Summarizing Polling Data
* Files can be found in the `PyPoll` folder
  * `main.py` = python script
  * `election_data.csv` = original data
  * `election_data_summary.csv` = summarized data created from the python script

* Taking a file containing votes for candidates, `main.py` summarizes the data. The results are printed to the terminal and a `.csv` file in the same directory as the script:
  * Total number of votes
  * A list of candidates with their corresponding number of votes and % of total votes
  * The winner
  
* Note that the headers and first two columns are not required, but the candidate's name must be in the third column:

![election_data](https://github.com/L0per/Python-Challenge/blob/master/Images/election_data.JPG?raw=true)

* The data is summarized in the terminal and `.csv` file as shown below:

![election_data_summary](https://github.com/L0per/Python-Challenge/blob/master/Images/election_summary.JPG?raw=true)
