# Write code so players can play tic tac toe. When a player (say player 1, who is X) wants to place an X on the screen,
# ask the user for a coordinate of where they want to place their piece.



reset = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game = reset


def top(game):
    return f" --- --- ---\n| {game[2][0]} | {game[2][1]} | {game[2][2]} |"


def top_start():
    return f"      ----- ----- -----\n   3 |(1,3)|(2,3)|(3,3)|"


def mid(game):
    return f"\n --- --- ---\n| {game[1][0]} | {game[1][1]} | {game[1][2]} |"


def mid_start():
    return f"\n      ----- ----- -----\nY: 2 |(1,2)|(2,2)|(3,2)|"


def bot(game):
    return f"\n --- --- ---\n| {game[0][0]} | {game[0][1]} | {game[0][2]} |"


def bot_start():
    return f"\n      ----- ----- -----\n   1 |(1,1)|(2,1)|(3,1)|"


def draw(game):
    return "".join(list((top(game), mid(game), bot(game))))


def welcome():
    print(
        "Welcome to Chloe's Tic Tac Toe!\nThe game board uses (x,y) coordinates as input to place your markers."
    )
    print("Enter your coordinates as 'x,y'. Don't include any spaces or parentheses.")
    print(
        "".join(
            list(
                [
                    top_start(),
                    mid_start(),
                    bot_start(),
                    "\n      ----- ----- -----",
                    "\nX:      1     2     3",
                ]
            )
        )
    )


welcome()

ready = input("Are you ready to play? (Type XXX at any time to exit) ")
ready = "yes"
while ready != "XXX":
    turn = "p1"
    while turn == "p1":
        coord_in = input("Player 1's turn. Enter your coordinates: ")
        coords = coord_in.split(",")
        x = int(coords[0])
        y = int(coords[1])
        if x > 3 or x < 1:
            print("Invalid number. X must be a 1, 2, or 3.")
            continue
        if y > 3 or y < 1:
            print("Invalid number. Y must be a 1, 2, or 3.")
            continue
        if game[y - 1][x - 1] == "O":
            print("Your opponent is occupying this spot!")
            continue
        elif game[y-1][x-1] == "X":
            print("You already placed an X here.")
            continue
        game[(y - 1)][(x - 1)] = "X"
        print(draw(game))
        turn = "p2"
    while turn == "p2":
        coord_in = input("Player 2's turn. Enter your coordinates: ")
        coords = coord_in.split(",")
        x = int(coords[0])
        y = int(coords[1])
        if x > 3 or x < 1:
            print("Invalid number. X must be a 1, 2, or 3.")
            continue
        if y > 3 or y < 1:
            print("Invalid number. Y must be a 1, 2, or 3.")
            continue
        if game[(y - 1)][(x - 1)] == "X":
            print("Your opponent is occupying this spot!")
            continue
        elif game[y - 1][x - 1] == "O":
            print("You already placed an O here.")
            continue
        game[(y - 1)][x - 1] = "O"
        print(draw(game))
        turn = "p1"
