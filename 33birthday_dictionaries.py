# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on
# their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user
# to enter a name, and return the birthday of that person back to them.

import json

birthdays = {
    "Chloe": "03/31/1990",
    "Stephen": "12/31/1985",
    "Pippin J. Marshmallow Bird": "10/24/2018",
    "Kalos P. Grumpy Bird": "06/15/2009",
    "Buena 'B'": "06/29/2009",
    "Famous Bid": "03/29/1999",
    "Silver": "01/22/2008",
}

with open("birthdays.json", "w") as f:
    json.dump(birthdays, f)


while True:
    inquiry = input("Enter a name: ").title()

    key_list = list(birthdays.keys())

    for key in key_list:
        if inquiry not in key:
            pass
            if key == key_list[-1]:
                print(f"Sorry, {inquiry} isn't in this dictionary.")
        else:
            print(f"{key}'s birthday is {birthdays[key]}")
            break
