# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# Extra 1: Keep the game going until the user types “exit”
# Extra 2: Keep track of how many guesses the user has taken, and when the game ends, print this out.
# Extra 3 (personal addition): Keep track of the highest and lowest score and print the results on exiting.
# Extra 4 (personal addition): Track and print all the guesses of the current round.

import random

num = random.randint(1,100)
guess_count = 1
scores = []
guesses = []

print("Welcome to the Guessing Game! A number has been selected.")

while True:
    if guesses != []:
        print(f"Previous guesses: {guesses}")
    elif guesses == []:
        pass
    guess = int(input("Enter a guess: "))

    if num > guess:
        print("Too low. Guess again.")
        if guess not in guesses:
            guesses.append(guess)
        guess_count +=1
        continue
    elif num < guess:
        print("Too high. Guess again.")
        if guess not in guesses:
            guesses.append(guess)
        guess_count +=1
        continue
    elif num == guess:
        print(f"Correct! The number was {num}.")
        print(f"It took you {guess_count} guesses.")
        if guess_count not in scores:
            scores.append(guess_count)
        play_again = input("Would you like to play again? Type 'exit' to end. ")
        if play_again != "exit":
            num = random.randint(1,100)
            guess_count = 1
            guesses.clear()
            print("New number selected.")
            continue
        else:
            print("Thanks for playing!")
            best_score = min(scores)
            worst_score = max(scores)
            print(f"Your best score was {best_score} guesses.")
            print(f"Your worst score was {worst_score} guesses.")
            break
