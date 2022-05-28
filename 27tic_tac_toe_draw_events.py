# Do exercise 27, using an event-driven approach.


def reset(game, turns_taken, state):
    game.clear()
    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turns_taken.clear()
    state = "play on"
    return game, turns_taken, state


def top(row):
    return f" --- --- ---\n| {row[0]} | {row[1]} | {row[2]} |"


def mid(row):
    return f"\n --- --- ---\n| {row[0]} | {row[1]} | {row[2]} |"


def bot(row):
    return f"\n --- --- ---\n| {row[0]} | {row[1]} | {row[2]} |\n --- --- ---"


def draw(turns_taken, game):
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


def change_player(curr_player):
    if curr_player == player_one:
        return player_two
    else:
        return player_one


def get_input(turns_taken):
    while True:
        # Get user input
        coords_in = input(f"{curr_player}'s turn. Enter your coordinates: ")

        # Input validation
        try:
            coords_xy = [int(coord) for coord in coords_in.split(",")]

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

        used_coords = {}
        coords = tuple(coords_xy)

        for turn in turns_taken:
            used_coords[turn["coords"]] = turn["player"]

        if coords not in used_coords:
            return coords
        elif curr_player == used_coords[coords]:
            print(f"You already put an {player_marks[curr_player]} here.")
            continue
        else:
            print("Your opponent is occupying this spot!")
            continue


def add_curr_turn(turns_taken, curr_player, coords):
    curr_turn = {
        "player": curr_player,
        "coords": coords,
    }
    turns_taken.append(curr_turn)


def check_state(game, player_marks, player_counts, turns_taken):

    win_conditions = {
        "top row": [
            game[2][0] == game[2][1] == game[2][2],
            [game[2][0], game[2][1], game[2][2]],
        ],
        "middle row": [
            game[1][0] == game[1][1] == game[1][2],
            [game[1][0], game[1][1], game[1][2]],
        ],
        "bottom row": [
            game[0][0] == game[0][1] == game[0][2],
            [game[0][0], game[0][1], game[0][2]],
        ],
        "first column": [
            game[2][0] == game[1][0] == game[0][0],
            [game[2][0], game[1][0], game[0][0]],
        ],
        "second column": [
            game[2][1] == game[1][1] == game[0][1],
            [game[2][1], game[1][1], game[0][1]],
        ],
        "third column": [
            game[2][2] == game[1][2] == game[0][2],
            [game[2][2], game[1][2], game[0][2]],
        ],
        "top-bottom diagonal": [
            game[2][0] == game[1][1] == game[0][2],
            [game[2][0], game[1][1], game[0][2]],
        ],
        "bottom-top diagonal": [
            game[0][0] == game[1][1] == game[2][2],
            [game[0][0], game[1][1], game[2][2]],
        ],
    }

    # Check for a winner
    for key, value in win_conditions.items():
        if value[0] and " " not in value[1]:
            player_counts[curr_player] += 1
            print(
                f"{curr_player} wins! They made a line of {player_marks[curr_player]}'s in the {key}."
            )
            return "game over"

    # Check for a draw
    if len(turns_taken) == 9:
        print("It's a draw!")
        return "game over"

    return "play on"


def setup():
    welcome()
    check_ready()

    return get_players()


player_one, player_two = setup()

game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
turns_taken = []
curr_player = None
state = "play on"

player_marks = {
    player_one: "X",
    player_two: "O",
}
player_counts = {
    player_one: 0,
    player_two: 0,
}


print("starting game...")

while True:
    while state == "play on":
        curr_player = change_player(curr_player)
        coords = get_input(turns_taken)
        add_curr_turn(turns_taken, curr_player, coords)
        draw(turns_taken, game)
        state = check_state(game, player_marks, player_counts, turns_taken)

        if state == "game over":
            ready = input("Would you like to play again? ")

            if ready.strip().lower() not in ["y", "yes", "ready", "ok", "1", "true"]:
                print("Thanks for playing! Here are your win tallies:")
                print(f"{player_one} wins: {player_counts[player_one]}")
                print(f"{player_two} wins: {player_counts[player_two]}")
                print("closing game...")
                exit()

            print(f"Starting a new game. Loser gets to go first!")
            game, turns_taken, state = reset(game, turns_taken, state)
