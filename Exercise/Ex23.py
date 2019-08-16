def print_horiz_line():
    print(" --- " * board_size)

def print_vert_line():
    print("|    " * (board_size + 1))


if __name__ == "__main__":
    board_size = int(input("What size of game board? "))

    for index in range(board_size):
        print_horiz_line()
        print_vert_line()
        print_horiz_line()



game = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]