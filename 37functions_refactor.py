# Refactor the following code:
    # print(" --- --- ---")
    # print("|   |   |   |")
    # print(" --- --- ---")
    # print("|   |   |   |")
    # print(" --- --- ---")
    # print("|   |   |   |")
    # print(" --- --- ---")

x = 18
y = 2

def horizontal_lines():
    print(" ---"*x)

def vertical_lines():
    print("".join(["|   |", "   |"*(x-1)]))

def draw():
    for _ in range(y):
        horizontal_lines()
        vertical_lines()
    horizontal_lines()

draw()
