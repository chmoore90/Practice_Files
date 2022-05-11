# Write a program (function!) that takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates.

import random
no_doubles = []
rand_list = []
n = 15
def remove_doubles(*list):
    for x in a:
        if x not in no_doubles:
            no_doubles.append(x)
        elif x in no_doubles:
            continue
    return no_doubles

def gen_rand_list(n, list):
    for x in range(n):
        list.append(random.randint(1,10))
    return list

a = gen_rand_list(n, rand_list)

print(a)
print(remove_doubles(a))
