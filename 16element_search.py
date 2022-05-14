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

def search_list(num, list):
    list_length = len(list)
    for x in range(list_length):
        if list[x] != num:
            continue
        else:
            return True
    return False

result = search_list(num, rand_list)

if result is True:
    print(f"Search result: Yes, {num} is in the list.")
else:
    print(f"Search result: Sorry, {num} is not listed.")


# Extra 1: Use binary search (both iterative and recursive)

def binary_iterative(num, list):
    low = 0
    mid = 0
    high = len(list) - 1

    if num < list[low]:
        return False
    if num > list[high]:
        return False
    else:
        while high >= low:
            mid = (high + low) // 2
            if num > list[mid]:
                low = mid + 1
            elif num < list[mid]:
                high = mid -1
            else:
                return True
        return False

result_it = binary_iterative(num, rand_list)

if result_it is True:
    print(f"Iterative result: Yes, {num} is in the list.")
else:
    print(f"Iterative result: Sorry, {num} is not listed.")


def binary_recursive(num, list, low, high):
    if high >= low:
        mid = (high + low) // 2
        if num == list[mid]:
            return True
        elif num > list[mid]:
            return binary_recursive(num, list, mid + 1, high)
        else:
            return binary_recursive(num, list, low, mid - 1)
    return False

result_rec = binary_recursive(num, rand_list, 0, len(rand_list) - 1)

if result_rec is True:
    print(f"Recursive result: Yes, {num} is in the list.")
else:
    print(f"Recursive result: Sorry, {num} is not listed.")
