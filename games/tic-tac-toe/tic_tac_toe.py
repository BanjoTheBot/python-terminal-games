"""
    Lachlan Paul, 2023
"""

import sys

row_1 = ["-", "-", "-"]
row_2 = ["-", "-", "-"]
row_3 = ["-", "-", "-"]
board = [row_1, row_2, row_3]

winners = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 4, 8],
    [2, 4, 6],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8]
]

# True is X's turn, False is O
turn = "X"


def main():
    global row_1, row_2, row_3, turn
    print("You will be prompted for row and then position")
    while True:
        try:
            print(*board, sep="\n")
            x_row = int(input(f"\n{turn}'s Row: "))
            x_row -= 1
            match x_row:
                case 0:
                    print(row_1)
                    row_1 = choose_position(row_1)
                case 1:
                    print(row_2)
                    row_2 = choose_position(row_2)
                case 2:
                    print(row_3)
                    row_3 = choose_position(row_3)
                case _:
                    continue

        except ValueError:
            print("Not a number")
            continue

        # check_for_win()

        if turn == "X":
            turn = "O"
        else:
            turn = "X"


def choose_position(row):
    """Used for choosing where the player's object will go"""
    global turn

    while True:
        try:
            pos = int(input(f"{turn}'s Position: "))
            pos -= 1

            if row[pos] != "-":
                print("Someone already has that spot!")
                continue

            print(pos)
            break
        except ValueError:
            print("Not a number")

    row[pos] = str(turn)

    return row


def check_for_win():
    """Checks to see if the stars(pieces) align"""
    global board, row_1, row_2, row_3, winners
    # x_yes = 0
    # o_yes = 0
    #
    # for value in winners:
    #     x_yes = 0
    #     o_yes = 0
    #     num_to_check = 0
    #
    #     print("haha")
    #     for number in value:
    #         if number > 2:
    #             number = 0
    #             break
    #         print(number)
    #         print(value)
    #         print("yoho", board[value[number]][number])
    #
    #         if board[value[number]][number] == "X":
    #             x_yes += 1
    #         elif board[value[number]][number] == "O":
    #             o_yes += 1
    #         else:
    #             break
    #
    #         if x_yes == 3:
    #             print("X Wins!")
    #             sys.exit(0)
    #         if o_yes == 3:
    #             print("O Wins!")
    #             sys.exit(0)
    #
    #         print("x", x_yes)
    #         print("o", o_yes)


if __name__ == "__main__":
    main()
