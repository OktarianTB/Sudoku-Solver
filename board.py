global_board = []


def convert_str_to_2d_board(str_board):
    game_board = []
    row = []
    for i in range(1, len(str_board)+1):
        if str_board[i-1] in "123456789":
            row.append(str_board[i-1])
        else:
            row.append("123456789")
        if i % 9 == 0:
            game_board.append(row)
            row = []
    return game_board


def print_board(game_board, debug=False):
    for i in range(len(game_board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        print(" ", end="")
        for j in range(len(game_board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if len(game_board[i][j]) == 1 or debug:
                print(game_board[i][j], end=" ")
            else:
                print("X", end=" ")
        print(end="\n")


def get_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
        return lines
    return None


def list_to_str(l):
    grid = ""
    for i in range(len(l)):
        for j in range(len(l)):
            grid += l[i][j]
    print(grid)
