# Write code so players can play tic tac toe. When a player (say player 1, who is X) wants to place an X on the screen,
# ask the user for a coordinate of where they want to place their piece.


<<<<<<< HEAD

reset = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game = reset
=======
reset = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game = reset

player_to_mark = {
    "Player 1": "X",
    "Player 2": "O",
}
mark_to_player = {
    "X": "Player 1",
    "O": "Player 2",
}
>>>>>>> d0a08ada77a0afe8c719a75b60fea046e5141e57


def top(game):
    return f" --- --- ---\n| {game[2][0]} | {game[2][1]} | {game[2][2]} |"


def mid(game):
    return f"\n --- --- ---\n| {game[1][0]} | {game[1][1]} | {game[1][2]} |"


<<<<<<< HEAD
def mid_start():
    return f"\n      ----- ----- -----\nY: 2 |(1,2)|(2,2)|(3,2)|"


=======
>>>>>>> d0a08ada77a0afe8c719a75b60fea046e5141e57
def bot(game):
    return f"\n --- --- ---\n| {game[0][0]} | {game[0][1]} | {game[0][2]} |"


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
                    "      ----- ----- -----\n   3 |(1,3)|(2,3)|(3,3)|",
                    "\n      ----- ----- -----\nY: 2 |(2,1)|(2,2)|(3,2)|",
                    "\n      ----- ----- -----\n   1 |(1,1)|(2,1)|(3,1)|",
                    "\n      ----- ----- -----",
                    "\nX:      1     2     3",
                ]
            )
        )
    )


def get_input(game, turn, player_to_mark):
    while turn in player_to_mark:
        xy_input = input(f"{turn}'s turn. Enter your coordinates: ")
        if xy_input == "XXX":
            turn = xy_input
            print("Thanks for playing!")
            return turn
        xy_list = xy_input.split(",")
        x = int(xy_list[0])
        y = int(xy_list[1])
        if x > 3 or x < 1:
            print("Invalid number. X must be a number 1, 2, or 3.")
            continue
        if y > 3 or y < 1:
            print("Invalud number. Y must be a number 1, 2, or 3.")
            continue
        game[(y - 1)][(x - 1)] = player_to_mark[turn]
        return game[(y - 1)][x - 1]


def change_players(turn):
    if turn == "Player 1":
        return "Player 2"
    if turn == "Player 2":
        return "Player 1"


welcome()

<<<<<<< HEAD
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
=======
turn = input("Are you ready to play? (Type XXX at any time to exit) ")
turn = "Player 1"
while turn != "XXX":
    get_input(game, turn, player_to_mark)
    print(draw(game))
    turn = change_players(turn)
>>>>>>> d0a08ada77a0afe8c719a75b60fea046e5141e57
