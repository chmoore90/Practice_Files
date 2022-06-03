# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on
# their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user
# to enter a name, and return the birthday of that person back to them.

birthdays = {
    "Chloe": "March 31, 1990",
    "Stephen": "December 31, 1985",
    "Pippin J. Marshmallow Bird": "October 24, 2018",
    "Kalos P. Grumpy Bird": "June 15, 2009",
    "Buena 'B'" : "June 29, 2009",
    "Famous Bid": "March 29, 1999",
    "Silver": "January 22, 2008",
}

inquiry = input("Enter a name: ").title()

key_list = list(birthdays.keys())
for key in key_list:
    if inquiry in key:
        print(f"{key}'s birthday is {birthdays[key]}")
