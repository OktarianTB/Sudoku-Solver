def convert_str_to_2d_board(str_board):
    board = []
    row = []
    for i in range(1, len(str_board)+1):
        if str_board[i-1] in "123456789":
            row.append(int(str_board[i-1]))
        else:
            row.append(0)
        if i % 9 == 0:
            board.append(row)
            row = []
    return board


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        print(" ", end="")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print(end="\n")


def get_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
        return lines
    return None

