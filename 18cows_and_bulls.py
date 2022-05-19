# cows = correct number, place
# bulls = correct number, wrong place

import random

size = 4
welcome = "Welcome to Cows and Bulls!"
message = "Enter a " + str(size) + " digit guess: "


def generate_num(size) -> str:
    num_list = [random.randint(0, 9) for _ in range(size)]
    return "".join(str(_) for _ in num_list)


def user_guess(message) -> str:
    return input(message)


def check_guess(num, size):
    cows, bulls = 0, 0

    for x in range(size):
        if guess[x] == num[x]:
            cows += 1
        elif guess[x] in num:
            bulls += 1

    return cows, bulls


print(welcome)
num = generate_num(size)

while True:
    guess = user_guess(message)
    cows, bulls = check_guess(num, size)

    print(f"cows: {cows}, bulls: {bulls}")

    if guess == num:
        print("You did it!")
        break
