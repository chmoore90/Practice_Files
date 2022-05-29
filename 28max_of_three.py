# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the
# Python max() function! (The goal of this exercise is to think about some internals that Python normally takes care of for us.
# All you need is some variables and if statements!)

import random

a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)


def find_max(a,b,c):
    hi = a
    if b >= a and b >= c:
        hi = b
    if c >= a and c >= b:
        hi = c
    return hi


print(a,b,c)
print(f"{find_max(a,b,c)} is the highest.")
