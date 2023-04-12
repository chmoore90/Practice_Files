# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any.
# A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

# Extra: Randomly generate game results to test

import random

play_list = [
    [],
    [],
    [],
]

for x in range(3):
    play_list[x].append(random.randint(0, 2))
    play_list[x].append(random.randint(0, 2))
    play_list[x].append(random.randint(0, 2))
print(play_list)


def check_plays():
    win_conditions = {
        "row one": play_list[0][0] == play_list[0][1] == play_list[0][2],
        "row two": play_list[1][0] == play_list[1][1] == play_list[1][2],
        "row three": play_list[2][0] == play_list[2][1] == play_list[2][2],
        "column one": play_list[0][0] == play_list[1][0] == play_list[2][0],
        "column two": play_list[0][1] == play_list[1][1] == play_list[2][1],
        "column three": play_list[0][2] == play_list[1][2] == play_list[2][2],
        "diagonal top-bottom": play_list[0][0] == play_list[1][1] == play_list[2][2],
        "diagonal bottom-top": play_list[2][0] == play_list[1][1] == play_list[0][2],
    }

    wins = []
    for condition, check in win_conditions.items():
        if check:
            wins.append(condition)
    if len(wins) == 0:
        print("Draw")
    else:
        print(f"Winning plays: {', '.join(wins)}")

check_plays()
