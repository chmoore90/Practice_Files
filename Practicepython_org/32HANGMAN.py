# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses
# (head, body, 2 legs, and 2 arms) before they lose the game. In Part 1, we loaded a random word list and picked a word
# from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user.
# In this exercise, we have to put it all together and add logic for handling guesses.
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# Optional additions:
# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
# This is challenging - do the other parts of the exercise first!
# Your solution will be a lot cleaner if you make use of functions to help you!

import requests
from bs4 import BeautifulSoup
import random
from hangman_art import *

limit = 6


def get_word():
    sowpods_url = "https://norvig.com/ngrams/sowpods.txt"

    r = requests.get(sowpods_url)
    soup = BeautifulSoup(r.text, "html.parser")

    sowpods = str(soup).splitlines()
    word = "".join(random.sample(sowpods, 1))

    return word


def check_guess(guess, word, game_letters):
    game_letters = list(game_letters)
    index = []

    for x in range(len(word)):
        try:
            index.append(word.index(guess, x, x + 1))
        except:
            pass

    for i in index:
        game_letters.pop(i)
        game_letters.insert(i, guess)

    if len(index) > 1:
        print(f"\nYes! There are {len(index)} {guess}'s.")
    else:
        print(f"\nYes! There is 1 {guess}.")

    game_letters = "".join(game_letters)

    return game_letters


def replay():
    replay = input("Do you want to play again? ")

    if replay.strip().lower() not in ["y", "yes", "ready", "ok", "1", "true"]:
        print("Thanks for playing!")
        exit()


while True:
    print("New word selected!")

    word = get_word()
    game_letters = "_" * len(word)
    guess_list = []
    guess_list_wrong = []

    while True:

        print(f"\n{game_letters}")
        draw_hangman(len(guess_list_wrong))
        print(
            f"You have {6 - len(guess_list_wrong)} lives - err, limbs remaining. Incorrect guesses: {', '.join(guess_list_wrong)}"
        )
        guess = input("Guess a letter: ").upper()

        if guess in guess_list:
            print(f"You've already guessed {guess}")
            continue

        if len(guess) != 1:
            print("Invalid guess. Please guess only one letter.")

            continue

        if not guess.isalpha():
            print("Invalid guess. Please enter a letter.")

            continue

        if guess not in word:
            print(f"No {guess}'s.")
            guess_list.append(guess)
            guess_list_wrong.append(guess)
            if len(guess_list_wrong) == limit:
                draw_hangman(len(guess_list_wrong))
                print(
                    f"Game over! You were too late for the hangman. The word was {word}."
                )
                replay()
                break

            continue

        guess_list.append(guess)

        new_letters = check_guess(guess, word, game_letters)
        game_letters = new_letters

        if game_letters == word:
            print(f"You got it! The word was {word}.")
            replay()
            break
