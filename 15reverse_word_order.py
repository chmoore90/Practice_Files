# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

def user_input():
    return input("Enter something: ")

def reverse_input(string):
    x = string.split()
    x.reverse()
    y = ' '.join(x)
    return y

user_message = user_input()
print(reverse_input(user_message))
