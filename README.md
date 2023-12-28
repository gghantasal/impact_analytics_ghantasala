### Impact Aanlytics Assignment

#### Question
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

#### Prerequisite
`Python 3` must be installed in your local machine.

#### How to run ?
To run the assignment execute following command:
```
python main.py 5
```
Here 5 can be replaced with desired number of days.

#### Approach
On any given day there could be two possibilties either you attend the classes or you miss the classes. I am generating all possible permutation of attending classes (i.e. 2 ^ No_of_days).

Next I am filtering all permutation which has 4 or more consecutive days of absence.

To compute probability I am simply dividing count of invalid permutation by total permutation.

**Time Complexity**: O(2 ^ N) where N is number of days.
