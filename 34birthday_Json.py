# In this exercise, modify your program from EX. 33 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file
# you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your
# JSON file should keep getting bigger and bigger.


import json

birthdays = {}

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)


while True:
    inquiry = input("Enter a name: ").title()

    key_list = list(birthdays.keys())

    for key in key_list:
        if inquiry not in key:
            pass

            if key == key_list[-1]:
                addon = input(
                    f"Sorry, {inquiry} isn't in this dictionary. Would you like to add a new entry? "
                )

                if addon.strip().lower() in ["y", "yes", "ok", "1", "true"]:
                    name = input(f"What is {inquiry}'s full name? ").title()
                    bday = input(f"What is {name}'s birthday? (Enter as: MM/DD/YYYY) ")
                    birthdays[name] = bday

                    with open("birthdays.json", "w") as f:
                        json.dump(birthdays, f)

                    print(f"{name}'s birthday was successfully added.")
                    break

                else:
                    break

        else:
            print(f"{key}'s birthday is {birthdays[key]}")
            break
