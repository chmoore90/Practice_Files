# In the exercise 34 we saved information about famous scientists’ names and birthdays to disk. In this exercise,
# load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday
# in each month.


import json
from collections import Counter


with open("birthdays.json", "r") as f:
    bdays = json.load(f)

months = []

print(bdays)
