import board
import copy as cp


def solve(game_board, iteration=0):
    empty_square = find_empty(game_board)
    if not empty_square:
        return True
    row, col = empty_square

    for i in game_board[row][col]:
        board_copy = cp.deepcopy(game_board)
        board_copy[row][col] = i
        if check_board_valid(board_copy):
            constraint_propagate(board_copy)

            if solve(board_copy, iteration+1):
                return True

    return False


def find_empty(game_board):
    """
    Returns an empty square in the board (denoted by 0) or None
    :type game_board: 2d list
    """
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if len(game_board[row][col]) == 2:
                return row, col
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if len(game_board[row][col]) >= 3:
                return row, col

    return None


def valid(game_board, value, row, col):
    """
    Checks the validity of the board after a new value has been inserted in the board
    :param value: digit that has been added to the new position (1-9)
    :param col: index of the column for the newly added value
    :param row: index of the row for the newly added value
    :type game_board: 2d list
    """
    if len(value) > 1:
        value = "X"
    # Check row of new position
    for i in range(len(game_board[row])):
        if game_board[row][i] == value and i != col:
            return False

    # Check column of new position
    for i in range(len(game_board)):
        if game_board[i][col] == value and i != row:
            return False

    # Check the 3x3 square area
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(start_row, start_row+3):
        for j in range(start_col, start_col+3):
            if game_board[i][j] == value and i != row and j != col:
                return False

    return True


def constraint_propagate(game_board):
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if len(game_board[i][j]) == 1:
                remove_nb_from_row(game_board, game_board[i][j], i)
                remove_nb_from_column(game_board, game_board[i][j], j)
                remove_nb_from_box(game_board, game_board[i][j], i, j)


def remove_nb_from_row(game_board, value, row):
    for i in range(len(game_board[row])):
        if game_board[row][i] != value:
            game_board[row][i] = game_board[row][i].replace(value, "")


def remove_nb_from_column(game_board, value, column):
    for i in range(len(game_board)):
        if game_board[i][column] != value:
            game_board[i][column] = game_board[i][column].replace(value, "")


def remove_nb_from_box(game_board, value, row, col):
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if game_board[i][j] != value:
                game_board[i][j] = game_board[i][j].replace(value, "")


def check_board_valid(game_board):
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if not valid(game_board, game_board[i][j], i, j):
                return False
    return True


# grid = "000158000002060800030000040027030510000000000046080790050000080004070100000325000"
# b = board.convert_str_to_2d_board(grid)
# board.print_board(b, True)
# print("")
# constraint_propagate(b)
# board.print_board(b, True)
# solve(b, True)
# print("")
# board.print_board(b, True)
