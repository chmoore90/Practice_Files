# Take two lists and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for x in a:
    if x in c:
        continue
    if x in b:
        c.append(x)

print(c)

# Extra 1: Randomly generate two lists to test this

import random
a.clear()
b.clear()
c.clear()

size1 = int(input("How long should list A be?"))
size2 = int(input("How long should list B be?"))

a = [random.randint(0,100) for x in range(size1)]
print(a)
b = [random.randint(0,100) for x in range(size2)]
print(b)

for x in a:
    if x in c:
        continue
    if x in b:
        c.append(x)
print(c)

# Extra 2: Write this in one line of Python

# ??
