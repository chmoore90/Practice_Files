# Do exercise 27, using an event-driven system.

reset = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game = reset


def top(row):
    return f" --- --- ---\n| {row[0]} | {row[1]} | {row[2]} |"


def mid(row):
    return f"\n --- --- ---\n| {row[0]} | {row[1]} | {row[2]} |"


def bot(row):
    return f"\n --- --- ---\n| {row[0]} | {row[1]} | {row[2]} |"


def draw(turns_taken):
    for turn in turns_taken:
        x, y = turn["coords"]
        game[y - 1][x - 1] = player_marks[turn["player"]]

    print("".join(list((top(game[2]), mid(game[1]), bot(game[0])))))


def welcome():
    print(
        "Welcome to Chloe's Tic Tac Toe!\nThe game board uses (x,y) coordinates as input to place your markers."
    )
    print(
        "Use a comma to separate x and y. You don't need to use any spaces or parentheses."
    )
    print(
        "".join(
            list(
                [
                    "      ----- ----- -----\n   3 |(1,3)|(2,3)|(3,3)|",
                    "\n      ----- ----- -----\nY: 2 |(1,2)|(2,2)|(3,2)|",
                    "\n      ----- ----- -----\n   1 |(1,1)|(2,1)|(3,1)|",
                    "\n      ----- ----- -----",
                    "\nX:      1     2     3",
                ]
            )
        )
    )


def check_ready():
    ready = input("Are you ready to start? ")

    if ready.strip().lower() not in ["y", "yes", "ready", "ok", "1", "true"]:
        print("players not ready, exiting...")
        exit()


def get_players():
    player_one = input("Enter player name for X: ")
    player_two = input("Enter player name for O: ")

    return player_one, player_two


def get_input(turns_taken):
    while True:
        # Get user input
        coords_in = input(f"{curr_player}'s turn. Enter your coordinates: ")

        # Input validation

        try:
            coords_xy = [int(coord) for coord in coords_in.split(",")]
            coords = tuple(coords_xy)

        except ValueError:
            print(
                "Invalid input. X and Y coordinates must be numbers (1, 2, or 3) and separated by a comma."
            )
            continue

        if len(coords_xy) != 2:
            print(
                "Invalid input. Coordinates must be two numbers, separated by a comma."
            )
            continue

        if coords_xy[0] > 3 or coords_xy[1] > 3 or coords_xy[0] < 1 or coords_xy[1] < 1:
            print("Invalid input. X and Y coordinates must be 1, 2, or 3.")
            continue

        used_coords = [turn["coords"] for turn in turns_taken]
        marks = [player_marks[turn["player"]] for turn in turns_taken]

        if coords in used_coords:
            print("This space is occupied!")
            continue
        return coords


def add_curr_turn(turns_taken, curr_player, coords):
    curr_turn = {
        "player": curr_player,
        "coords": coords,
    }
    turns_taken.append(curr_turn)


def change_player(curr_player):
    if curr_player == player_one:
        curr_player = player_two
    else:
        curr_player = player_one
    return curr_player


def setup():
    welcome()
    check_ready()

    return get_players()


turns_taken = []
player_one, player_two = setup()
player_marks = {
    player_one: "X",
    player_two: "O",
}
curr_player = player_one

print("starting game...")
while True:
    coords = get_input(turns_taken)
    add_curr_turn(turns_taken, curr_player, coords)
    draw(turns_taken)
    curr_player = change_player(curr_player)
