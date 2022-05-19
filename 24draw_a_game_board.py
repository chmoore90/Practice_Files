# Time for some fake graphics! Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

from asyncore import close_all


def hor():
    return " ---"

def one_mid():
    return "|"

def vert():
    return "   |"

def create_top(x):
    return ''.join([hor()*x, "\n", one_mid(), vert()*x, "\n", hor()*x])

def create_bot(x):
    return ''.join(["\n", one_mid(), vert()*x, "\n", hor()*x])

def create_board(x, y):
        board = ''.join([create_top(x), (create_bot(x))*(y-1)])
        return board


columns = int(input("Enter number of columns: "))
rows = int(input("Enter number of rows: "))

b = create_board(columns, rows)


print(b)

