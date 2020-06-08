from copy import deepcopy
from random import randint
from board import print_board

grid = [['1', '5', '2', '9', '3', '4', '6', '8', '7'],
        ['7', '6', '3', '8', '2', '1', '5', '4', '9'],
        ['9', '8', '4', '5', '6', '7', '3', '2', '1'],
        ['6', '1', '8', '4', '9', '3', '2', '7', '5'],
        ['3', '7', '5', '1', '8', '2', '4', '9', '6'],
        ['2', '4', '9', '7', '5', '6', '8', '1', '3'],
        ['5', '2', '1', '3', '7', '8', '9', '6', '4'],
        ['4', '3', '6', '2', '1', '9', '7', '5', '8'],
        ['8', '9', '7', '6', '4', '5', '1', '3', '2']]


def create_permuted_board():
    game_board = grid
    # Randomize board by permuting rows, columns & rotating (no effect on whether the board is solvable)
    for i in range(randint(20, 25)):
        permutation_index = randint(0, 5)
        if permutation_index == 0:
            switch_numbers(game_board, randint(1, 9), randint(1, 9))
        if permutation_index == 1:
            index1 = randint(0, 2) * 3
            index2 = index1 + randint(0, 2)
            index1 += + randint(0, 2)
            switch_column(game_board, index1, index2)
        if permutation_index == 2:
            index1 = randint(0, 2) * 3
            index2 = index1 + randint(0, 2)
            index1 += + randint(0, 2)
            switch_row(game_board, index1, index2)
        if permutation_index == 3:
            index1 = randint(0, 2)
            index2 = randint(0, 2)
            switch_block_column(game_board, index1, index2)
        if permutation_index == 4:
            index1 = randint(0, 2)
            index2 = randint(0, 2)
            switch_block_row(game_board, index1, index2)
        if permutation_index == 5:
            rotate_clockwise(game_board)
    print_board(game_board)
    # Randomly remove some values from the board
    min_values = 9
    current_values = len(game_board) * len(game_board[0])
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if randint(0, 4) != 0 and current_values > min_values:
                game_board[i][j] = "123456789"
                current_values -= 1

    return game_board


def switch_numbers(game_board, nb1, nb2):
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == nb1:
                game_board[i][j] = nb2
            if game_board[i][j] == nb2:
                game_board[i][j] = nb1


def switch_column(game_board, index1, index2):
    copy_board = deepcopy(game_board)
    for i in range(len(game_board)):
        game_board[i][index1] = copy_board[i][index2]
        game_board[i][index2] = copy_board[i][index1]


def switch_row(game_board, index1, index2):
    copy_board = deepcopy(game_board)
    game_board[index1] = copy_board[index2]
    game_board[index2] = copy_board[index1]


def switch_block_column(game_board, index1, index2):
    copy_board = deepcopy(game_board)
    for i in range(len(game_board)):
        game_board[i][index1*3] = copy_board[i][index2*3]
        game_board[i][index1*3+1] = copy_board[i][index2*3+1]
        game_board[i][index1*3+2] = copy_board[i][index2*3+2]
        game_board[i][index2*3] = copy_board[i][index1*3]
        game_board[i][index2*3+1] = copy_board[i][index1*3+1]
        game_board[i][index2*3+2] = copy_board[i][index1*3+2]


def switch_block_row(game_board, index1, index2):
    copy_board = deepcopy(game_board)
    for i in range(len(game_board)):
        game_board[index1*3] = copy_board[index2*3]
        game_board[index1*3+1] = copy_board[index2*3+1]
        game_board[index1*3+2] = copy_board[index2*3+2]
        game_board[index2*3] = copy_board[index1*3]
        game_board[index2*3+1] = copy_board[index1*3+1]
        game_board[index2*3+2] = copy_board[index1*3+2]


def rotate_clockwise(game_board):
    n = len(game_board[0])
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = game_board[i][j]
            game_board[i][j] = game_board[n - 1 - j][i]
            game_board[n - 1 - j][i] = game_board[n - 1 - i][n - 1 - j]
            game_board[n - 1 - i][n - 1 - j] = game_board[j][n - 1 - i]
            game_board[j][n - 1 - i] = temp
