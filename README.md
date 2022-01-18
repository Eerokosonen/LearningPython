# Learning Python
How I learned a little bit of Python during an eye tracking course

## Assignment

As a part of an eye tracking course, we got an assignment to use a deep neural network called U'n'Eye to analyze raw eye tracker data, and detect eye fixations.

U'n'Eye repository can be found here: 
https://github.com/berenslab/uneye

We got a dataset, but it was not in a correct format for U'n'Eye to analyze.


## Problem I had to solve:

U'n'Eye python package needs eye tracker data as distinct files: y-values as one csv file, and x-values as one. The dataset we got for this assignment was not in the correct format, it had some unnecessary values for this calculation. 
It was a csv file with the formatting: 'subjectnumber,unnecessary_value,xvalue_1,yvalue_1,xvalue_2,yvalue_2,...,xvalue_n,yvalue_n'

There were multiple subjects, and multiple sessions per subject. In this assignment we had to analyze all sessions per given subjects.

### Problem 1: 
I had to solve was to go trough the csv file, select the needed lines or subjects, and parse the x and y values to distinct files. 

### Problem 2:
After I ran the U'n'Eye script, I got the calculations of fixations. They were also not in the correct format, and from this data the total fixation count, and average fixation duration had to be calculated

## How I solved it:

### Problem 1:
The solution can be found in file: parsing.py. With this script, the needed subject (one subject has multiple lines in the csv) has to be chosen, and the script goes through all the lines, and extracts x and y values to csv files, for U'n'Eye to analyze.

### Problem 2:
The solution can be found in file: count_fixations.py. With this script, the U'n'Eye output file has to be selected first, for the script to go through the file and perform fixation calculations. 

