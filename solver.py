import copy as cp
import time
import board as b


def solve_sudoku(game_board, demo=False):
    empty_square = find_empty(game_board)
    if not empty_square:
        return True
    row, col = empty_square
    print(row, col)
    for i in game_board[row][col]:
        board_copy = cp.deepcopy(game_board)
        b.global_board = cp.deepcopy(board_copy)
        board_copy[row][col] = i
        if demo:
            time.sleep(0.02)
        if check_board_valid(board_copy):
            constraint_propagate(board_copy, demo)
            b.global_board = cp.deepcopy(board_copy)

            if solve_sudoku(board_copy, demo):
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


def constraint_propagate(game_board, demo=False):
    for i in range(len(game_board)):
        if demo:
            time.sleep(0.02)
        for j in range(len(game_board[i])):
            if len(game_board[i][j]) == 1:
                if demo:
                    b.global_board = cp.deepcopy(game_board)
                remove_nb_from_row(game_board, game_board[i][j], i, demo)
                if demo:
                    b.global_board = cp.deepcopy(game_board)
                remove_nb_from_column(game_board, game_board[i][j], j, demo)
                if demo:
                    b.global_board = cp.deepcopy(game_board)
                remove_nb_from_box(game_board, game_board[i][j], i, j, demo)


def remove_nb_from_row(game_board, value, row, demo=False):
    for i in range(len(game_board[row])):
        if game_board[row][i] != value:
            game_board[row][i] = game_board[row][i].replace(value, "")
            if demo:
                b.global_board = cp.deepcopy(game_board)
                time.sleep(0.005)


def remove_nb_from_column(game_board, value, column, demo=False):
    for i in range(len(game_board)):
        if game_board[i][column] != value:
            game_board[i][column] = game_board[i][column].replace(value, "")
            if demo:
                b.global_board = cp.deepcopy(game_board)
                time.sleep(0.005)


def remove_nb_from_box(game_board, value, row, col, demo=False):
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if game_board[i][j] != value:
                game_board[i][j] = game_board[i][j].replace(value, "")
                if demo:
                    b.global_board = cp.deepcopy(game_board)
                    time.sleep(0.005)


def check_board_valid(game_board):
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if not valid(game_board, game_board[i][j], i, j):
                return False
    return True
