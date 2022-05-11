# # Write a program (function!) that takes a list and returns a new list that contains all the elements
# # of the first list minus all the duplicates.

# # Extra 1a: Write two different functions to do this - one using a loop and constructing a list...

# import random
# no_doubles = []
# rand_list = []
# n = 15

# def remove_doubles(*list):
#     for x in a:
#         if x not in no_doubles:
#             no_doubles.append(x)
#         elif x in no_doubles:
#             continue
#     return no_doubles

# def gen_rand_list(n, list):
#     for x in range(n):
#         list.append(random.randint(1,10))
#     return list

# a = gen_rand_list(n, rand_list)

# print(a)
# print(remove_doubles(a))


# # Extra 1b: ...and another using sets.

# b = set(a)
# print(b)


# Extra 2: Go back and do Exercise 5 using sets, and write the solution for that in a different function.
# "Take two lists and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes."

import random

x = set()
y = set()
z = set()

size1 = int(input("How long should set X be? "))
size2 = int(input("How long should set Y be? "))

def gen_rand_set():


x = set.add(random.sample(range(0,100), size1))
print(x)
y = set([random.sample(range(0,100), size2)])
print(y)
