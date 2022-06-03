# In the exercise 34 we saved information about famous scientists’ names and birthdays to disk. In this exercise,
# load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday
# in each month.


import json
from collections import Counter
import calendar


with open("birthdays.json", "r") as f:
    bdays = json.load(f)

months = []

for value in bdays.values():
    month_no = int(value.split("/")[0])
    month = calendar.month_name[month_no]
    months.append(month)

month_count = Counter(months)

print(month_count)
