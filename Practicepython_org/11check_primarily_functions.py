# Ask the user for a number and determine whether the number is prime or not.

def get_num():
    return int(input("Enter a number: "))

def check_primarity():
    for x in range(2,(num//2+1)):
        if num%x != 0:
            continue
        elif num%x == 0:
            return False


num = get_num()
check_num = check_primarity()

if check_num is False:
    print(f"{num} is NOT a prime number.")
else:
    print(f"{num} is a prime number!")
