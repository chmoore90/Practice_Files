# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it. This time, we’re going to do exactly the opposite.
# You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number.


print("Let's set up the range of number for the guessing game!")
low_in = int(input("Enter the lowest number: "))
high_in = int(input("Enter the highest number: "))
low = low_in
high = high_in
size = high_in - low_in
num = (size // 2) + low


def reset():
    global low
    global high
    global size
    global num

    low = low_in
    high = high_in
    size = high_in - low_in
    num = (size // 2) + low


resp = input("Have you picked your number? (Or type 'END' to exit): ")

while True:
    if resp == "END":
        print("Thanks for playing!")
        break

    resp = input(f"Is your number {num}? ")

    if resp == "higher":
        low = num
        size = high - low
        num = (size // 2) + low

    elif resp == "lower":
        high = num
        size = high - low
        num = (size // 2) + low

    elif resp == "yes":
        resp = input(f"Hooray! The number was {num} Do you want to play again? ")
        reset()
