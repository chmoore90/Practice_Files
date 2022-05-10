# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.

# Extra 1: Keep the game going until the user types “exit”

# Extra 2: Keep track of how many guesses the user has taken, and when the game ends, print this out.

# Extra 3 (personal addition): Keep track of the highest and lowest score and print the results on exiting.

import random

num = random.randint(1,100)
guess_count = 1

while True:
    guess = int(input("Enter a guess: "))

    if num > guess:
        print("Too low. Guess again.")
        guess_count +=1
        continue
    elif num < guess:
        print("Too high. Guess again.")
        guess_count +=1
        continue
    elif num == guess:
        print(f"Correct! The number was {num}.")
        print(f"It took you {guess_count} guesses.")
        play_again = input("Would you like to play again? Type 'exit' to end. ")
        if play_again != "exit":
            num = random.randint(1,100)
            guess_count = 1
            print("New number selected.")
            continue
        else:
            print("Thanks for playing!")
            break
