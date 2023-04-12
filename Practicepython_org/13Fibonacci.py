# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

def get_length():
    return int(input("How many numbers? "))

def gen_fib (num):
    if num > 2:
        for x in range(2,num):
            fib.append(fib[x-1]+fib[x-2])
            continue
    elif num == 2:
        return [1,1]
    elif num == 1:
        return [1]
    return fib

fib = [1,1]
num = get_length()
print(gen_fib(num))
