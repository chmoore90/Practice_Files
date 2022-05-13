# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
# and another number. The function decides whether or not the given number is inside the list and returns (then prints)
# an appropriate boolean.

import random

size = 10
rand_list = []

def rand_list_generator(size, list):
    for x in range(size):
        list.append(random.randint(0,20))
    list.sort()
    return list

def rand_num_generator():
    return random.randint(0,20)

rand_list = rand_list_generator(size, rand_list)
num = rand_num_generator()

print(rand_list)
print(num)

if num in rand_list:
    print(f"Yes, {num} is in the list.")
else:
    print(f"Sorry, {num} is not listed.")

# Extra 1: Use binary search

def binary_search(num, list):
    list_length = len(list)
    for x in range(list_length):
        if list[x] != num:
            continue
        else:
            return True
    return False

result = binary_search(num, rand_list)

if result is True:
    print(f"Yes, {num} is in the list.")
else:
    print(f"Sorry, {num} is not listed.")
