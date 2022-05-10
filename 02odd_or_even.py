# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

num = int(input("Enter a number: "))

if num%2 == 0:
    print(f"{num} is even.")
elif num%2 != 0:
    print(f"{num} is odd.")
