import board


def solve(game_board):
    empty_square = find_empty(game_board)
    if not empty_square:
        return True
    row, col = empty_square

    for i in range(1, len(game_board[0]) + 1):
        if valid(game_board, i, row, col):
            game_board[row][col] = i

            if solve(game_board):
                return True

            game_board[row][col] = 0

    return False


def find_empty(game_board):
    """
    Returns an empty square in the board (denoted by 0) or None
    :type game_board: 2d list
    """
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if game_board[row][col] == 0:
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


grid_str = '85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4.'
game_board = board.convert_str_to_2d_board(grid_str)
board.print_board(game_board)
successful = solve(game_board)
print(" ")

if not successful:
    print("Failed!")
else:
    board.print_board(game_board)