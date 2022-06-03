# In this exercise, modify your program from EX. 33 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file
# you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your
# JSON file should keep getting bigger and bigger.

import json

birthdays = {
    "Chloe": "March 31, 1990",
    "Stephen": "December 31, 1985",
    "Pippin J. Marshmallow Bird": "October 24, 2018",
    "Kalos P. Grumpy Bird": "June 15, 2009",
    "Buena 'B'" : "June 29, 2009",
    "Famous Bid": "March 29, 1999",
    "Winnie": "October 3, 2020",
    "Robin": "August 9, 2020",
    "Silver": "January 22, 2008",
}

with open("birthdays.json", "w") as f:
    json.dump(birthdays, f)
