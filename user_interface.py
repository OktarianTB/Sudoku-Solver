import pygame
import board as b
import solver as sv
import copy as cp
import threading
from time import sleep

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
                if len(self.cubes[i][j].value) > 1:
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

        if len(self.value) > 1:
            text = fnt.render("", 1, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        else:
            text = fnt.render(str(self.value), 1, (0, 0, 0))
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
    grid = "000003017015009008060000000100007000009000200000500004000000020500600340340200000"
    game_board = b.convert_str_to_2d_board(grid)
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
                    thread1 = SolverThread(1, game_board)
                    thread1.start()
                    started = True

        if board.is_finished():
            print("Game over")
            run = False
            sleep(5)

        if started:
            game_board = cp.deepcopy(b.global_board)
            board.cubes = [[Cube(game_board[i][j], i, j, 540, 540) for j in range(len(game_board[0]))]
                           for i in range(len(game_board))]
        redraw_window(win, board)
        pygame.display.update()


main()
pygame.quit()
