# Do exercise 27, using an event-driven system.

reset = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game = reset


def top(game):
    return f" --- --- ---\n| {game[2][0]} | {game[2][1]} | {game[2][2]} |"


def mid(game):
    return f"\n --- --- ---\n| {game[1][0]} | {game[1][1]} | {game[1][2]} |"


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


def check_ready():
    ready = input("are you ready")

    return ready.strip().lower() in ["y", "yes", "ready", "ok", "1", "true"]


def get_players():
    player_one = input("name of player one")
    player_two = input("name of player two")

    return player_one, player_two

# turn = {
#     "player": 1,
#     "coords": (0, 0),
# }

turns_taken = []

welcome()

if not check_ready():
    print("players not ready, exiting...")
    exit()

while True:
    print("starting game...")
    break
