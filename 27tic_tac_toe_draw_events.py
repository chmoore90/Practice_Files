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

    if ready.strip().lower() not in ["y", "yes", "ready", "ok", "1", "true"]:
        print("players not ready, exiting...")
        exit()


def get_players():
    player_one = input("name of player one")
    player_two = input("name of player two")

    return player_one, player_two

def get_input(turns_taken):
    while True:
        coords = tuple([int(coord) for coord in input("enter coords").split(",")])
        used_coords = [turn["coords"] for turn in turns_taken]
        marks = [player_marks[turn["player"]] for turn in turns_taken]

        for i in range(len(used_coords)):
            used_coord = used_coords[i]
            mark = marks[i]

            if coords == used_coord:
                print("can't do that")
                print(mark)

        return coords

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
    # coords = get_input(turns_taken)

    #

    # take_turn(turns_taken, curr_player, coords)
    curr_turn = {
        "player": curr_player,
        "coords": coords,
    }

    turns_taken.append(curr_turn)
    #

    draw(turns_taken)

    # curr_player = switch_player(curr_player)
    if curr_player == player_one:
        curr_player = player_two
    else:
        curr_player = player_one
    #
