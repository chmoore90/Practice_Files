# Remake of Mom's word game. Similar to Cows and Bulls, guess a word by guessing other words and seeing what letters are in the
# correct spot. Cow = right letter, right place. Bull = right letter, wrong place.

import random


length = 5
game_words = []


def get_word(length, game_words):
    with open("sowpods.txt", "r") as sowpods_dict:
        sowpods = sowpods_dict.read()

    all_words = sowpods.splitlines()

    for i in range(len(all_words)):
        if len(all_words[i]) == length:
            game_words.append(all_words[i])

    word = "".join(random.sample(game_words, 1))

    return word, game_words


while True:

    word, game_words = get_word(length, game_words)
    print(word)


    while True:

        guess = input(f"Enter a {length} letter word: ").upper()
        display = []

        if guess not in game_words:
            print(f"Invalid entry.")
            continue

        for i in range(length):

            if guess[i] == word[i]:
                display.append(word[i])
            elif guess[i] not in word:
                display.append("-")
            else:
                display.append("+")

        print("".join(display))

        if guess == word:
            print(f"Yes! The word was {word}.")

            replay = input("Do you want to play again? ")
            if replay.strip().lower() not in ["y", "yes", "ready", "ok", "1", "true"]:
                print("Thanks for playing!")
                exit()

            break
