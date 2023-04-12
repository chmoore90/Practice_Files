# Take two lists and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Write this using at least one list comprehension.

import random

size1 = int(input("How long should list A be? "))
size2 = int(input("How long should list B be? "))
a = [random.randint(0,100) for x in range(size1)]
b = [random.randint(0,100) for x in range(size2)]
print(a)
print(b)

c = {x for x in a if x in b}
print(c)
