# Write code so players can play tic tac toe. When a player (say player 1, who is X) wants to place an X on the screen,
# ask the user for a coordinate of where they want to place their piece.



reset = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game = reset


def top(game):
    return f" --- --- ---\n| {game[0][0]} | {game[0][1]} | {game[0][2]} |"


def top_start():
    return f"      ----- ----- -----\n   3 |(1,3)|(2,3)|(3,3)|"


def mid(game):
    return f"\n --- --- ---\n| () | {game[1][1]} | {game[1][2]} |"


def mid_start():
    return f"\n      ----- ----- -----\nY: 2 |(2,1)|(2,2)|(3,2)|"


def bot(game):
    return f"\n --- --- ---\n| {game[2][0]} | {game[2][1]} | {game[2][2]} |"


def bot_start():
    return f"\n      ----- ----- -----\n   1 |(1,1)|(2,1)|(3,1)|"


def draw(game):
    return "".join(list((top(game), mid(game), bot(game))))

game_board = {
    ""
}


# def welcome():
#     print(
#         "Welcome to Chloe's Tic Tac Toe!\nThe game board uses (x,y) coordinates as input to place your markers:"
#     )
#     print(
#         "".join(
#             list(
#                 [
#                     top_start(),
#                     mid_start(),
#                     bot_start(),
#                     "\n      ----- ----- -----",
#                     "\nX:      1     2     3",
#                 ]
#             )
#         )
#     )
#     print("Enter your coordinates as 'x,y'. Don't include any spaces or parentheses.")


# welcome()

# ready = input("Are you ready to play? (Type XXX to exit) ")
# while ready != "XXX":
#     pass


def play():
    coors = input("Enter your coordinates: ")
    coorl = coors.split(',')
    x = coorl[0]
    y = coorl[1]
    print(x,y)

play()
