# For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were
# guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. As a bonus,
# keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
# Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or
# keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.

import random


def get_word():
    with open("sowpods.txt", "r") as sowpods_dict:
        sowpods = sowpods_dict.read()
    word = "".join(random.sample(sowpods.split(), 1))
    return word


def check_guess(guess, word, game_letters):
    game_letters = list(game_letters)
    index = []

    for x in range(len(word)):
        try:
            index.append(word.index(guess, x, x + 1))
        except:
            pass
    print(index)

    for i in index:
        game_letters.pop(i)
        game_letters.insert(i, guess)

    game_letters = ''.join(game_letters)

    return game_letters


word = get_word()
print(word)

game_letters = "_" * len(word)
print(game_letters)

while True:
    guess = input("Guess a letter: ").upper()

    if guess not in word:
        print(f"no {guess}")
        continue

    print(game_letters)
    new_letters = check_guess(guess, word, game_letters)
    game_letters = new_letters
    print(game_letters)
