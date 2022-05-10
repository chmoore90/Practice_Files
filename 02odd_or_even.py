# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

num = int(input("Enter a number: "))

if num%2 == 0:
    print(f"{num} is even.")
elif num%2 != 0:
    print(f"{num} is odd.")

# Extra 1:
# If the number is a multiple of 4, print out a different message.

if num%4 == 0:
    print(f"{num} is also divisible by 4.")

# Extra 2:
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num1 = int(input("Enter a new number: "))
check = int(input("Enter another number: "))

if num1%check == 0:
    print(f"{check} divides evenly into {num1}.")
elif num1%check != 0:
    print(f"{check} does not divide evenly into {num1}.")
