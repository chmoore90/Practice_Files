# # Write a program (function!) that takes a list and returns a new list that contains all the elements
# # of the first list minus all the duplicates.

# # Extra 1a: Write two different functions to do this - one using a loop and constructing a list...

import random
# no_doubles = []
# rand_list = []
# size = 15

# def remove_doubles(*list):
#     for x in a:
#         if x not in no_doubles:
#             no_doubles.append(x)
#         elif x in no_doubles:
#             continue
#     return no_doubles

# def gen_rand_list(size, list):
#     for x in range(size):
#         list.append(random.randint(1,10))
#     return list

# a = gen_rand_list(size, rand_list)

# print(a)
# print(remove_doubles(a))


# # Extra 1b: ...and another using sets.

# b = set(a)
# print(b)


# Extra 2: Go back and do Exercise 5 using sets, and write the solution for that in a different function.
# "Take two lists and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes."


x = set()
y = set()
z = set()

size1 = 20
size2 = 15

def gen_rand_set(set: set):
    for _ in range(size1):
        set.add(random.randint(1,30))
    return set

x = gen_rand_set(x)
print(x)
y = gen_rand_set(y)
print(y)

z = x.intersection(y)
print(z)

x.intersection_update(y)
print(x)
