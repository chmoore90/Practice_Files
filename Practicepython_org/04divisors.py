# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("Enter a number: "))
divisors = []

for x in range(2,(num//2+1)):
    if num%x == 0:
        divisors.append(x)
divisors.insert(0,1)
divisors.append(num)

print(divisors)
