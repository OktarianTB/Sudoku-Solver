import pygame
import board as b
import solver as sv
import copy as cp
import threading
from time import sleep
from generator import create_permuted_board

pygame.font.init()


class Grid:
    def __init__(self, game_board, width, height):
        self.rows = len(game_board)
        self.cols = len(game_board[0])
        self.cubes = [[Cube(game_board[i][j], i, j, width, height) for j in range(len(game_board[0]))]
                      for i in range(len(game_board))]
        self.width = width
        self.height = height

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if len(self.cubes[i][j].value) > 1 and "S" not in self.cubes[i][j].value:
                    return False
        return True


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render("PRESS ENTER TO START", 1, (0, 0, 0))
        win.blit(text, (100, 560))

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        fnt = pygame.font.SysFont("comicsans", 40)

        if len(self.value) > 1 and self.value[1] != "S":
            text = fnt.render("", 1, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        elif len(self.value) == 1:
            text = fnt.render(self.value[0], 1, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        else:
            text = fnt.render(self.value[0], 1, (255, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))


def redraw_window(win, board):
    win.fill((255, 255, 255))
    board.draw(win)


class SolverThread(threading.Thread):
    def __init__(self, thread_id, game_board):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.game_board = game_board

    def run(self):
        sv.solve_sudoku(self.game_board, True)


def main():
    game_board = create_permuted_board()
    solvable_game_board = cp.deepcopy(game_board)

    # Adding a 'S' to the end of the values the board starts with to color them in red
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if len(game_board[i][j]) == 1:
                game_board[i][j] = game_board[i][j] + "S"

    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Grid(game_board, 540, 540)
    run = True
    started = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not started:
                    thread1 = SolverThread(1, solvable_game_board)
                    thread1.start()
                    started = True

        if board.is_finished():
            run = False
            sleep(5)

        if started:
            game_board = cp.deepcopy(b.global_board)
            for i in range(len(game_board)):
                for j in range(len(game_board[i])):
                    if board.cubes[i][j].value != game_board[i][j] and "S" not in board.cubes[i][j].value:
                        board.cubes[i][j] = Cube(game_board[i][j], i, j, 540, 540)

        redraw_window(win, board)
        pygame.display.update()


main()
pygame.quit()
