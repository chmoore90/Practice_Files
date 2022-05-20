# Write code so players can play tic tac toe. When a player (say player 1, who is X) wants to place an X on the screen,
# ask the user for a coordinate of where they want to place their piece.

# From exercise 24:


def top():
    return ''.join([" --- --- ---", "\n", "| game[0][0]"


def one_mid():
    return "|"


def vert():
    return f" {game[x]} |"


def create_top(x):
    return "".join([hor() * x, "\n", one_mid(), vert() * x, "\n", hor() * x])


def create_bot(x):
    return "".join(["\n", one_mid(), vert() * x, "\n", hor() * x])


def create_board(x, y):
    board = "".join([create_top(x), (create_bot(x)) * (y - 1)])
    return board


columns = 3
rows = 3
x = " "
b = create_board(columns, rows)


print(b)

game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(game)
