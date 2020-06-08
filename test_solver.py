import unittest
import board
import solver
import generator
from random import randint


class TestSolver(unittest.TestCase):

    def check(self, lines):
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            result = solver.solve_sudoku(game_board, False)
            print(result)
            self.assertEqual(result, True)

    def test_easy1(self):
        lines = board.get_lines("sudoku_boards/easy1.txt")
        self.check(lines)

    def test_easy2(self):
        lines = board.get_lines("sudoku_boards/easy2.txt")
        self.check(lines)

    def test_easy3(self):
        lines = board.get_lines("sudoku_boards/easy3.txt")
        self.check(lines)

    def test_easy4(self):
        lines = board.get_lines("sudoku_boards/easy4.txt")
        self.check(lines)

    def test_easy5(self):
        lines = board.get_lines("sudoku_boards/easy5.txt")
        self.check(lines)

    def test_hardest(self):
        lines = board.get_lines("sudoku_boards/hardest.txt")
        self.check(lines)

    def test_switch_numbers(self):
        lines = board.get_lines("sudoku_boards/hardest.txt")
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            for _ in range(10):
                generator.switch_numbers(game_board, randint(1, 9), randint(1, 9))
            result = solver.solve_sudoku(game_board, False)
            self.assertEqual(result, True)

    def test_switch_columns(self):
        lines = board.get_lines("sudoku_boards/hardest.txt")
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            for _ in range(10):
                index1 = randint(0, 2) * 3
                index2 = index1 + randint(0, 2)
                index1 += randint(0, 2)
                generator.switch_column(game_board, index1, index2)
            result = solver.solve_sudoku(game_board, False)
            self.assertEqual(result, True)

    def test_switch_row(self):
        lines = board.get_lines("sudoku_boards/hardest.txt")
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            for _ in range(10):
                index1 = randint(0, 2) * 3
                index2 = index1 + randint(0, 2)
                index1 += randint(0, 2)
                generator.switch_row(game_board, index1, index2)
            result = solver.solve_sudoku(game_board, False)
            self.assertEqual(result, True)

    def test_switch_block_column(self):
        lines = board.get_lines("sudoku_boards/hardest.txt")
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            for _ in range(10):
                index1 = randint(0, 2)
                index2 = randint(0, 2)
                generator.switch_block_column(game_board, index1, index2)
            result = solver.solve_sudoku(game_board, False)
            self.assertEqual(result, True)

    def test_switch_block_row(self):
        lines = board.get_lines("sudoku_boards/hardest.txt")
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            for _ in range(10):
                index1 = randint(0, 2)
                index2 = randint(0, 2)
                generator.switch_block_row(game_board, index1, index2)
            result = solver.solve_sudoku(game_board, False)
            self.assertEqual(result, True)

    def test_rotate_clockwise(self):
        lines = board.get_lines("sudoku_boards/hardest.txt")
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            generator.rotate_clockwise(game_board)
            result = solver.solve_sudoku(game_board, False)
            self.assertEqual(result, True)

    def test_get_base_grid(self):
        for _ in range(20):
            game_board = generator.get_base_grid()
            result = solver.solve_sudoku(game_board, False)
            self.assertEqual(result, True)

    def test_generator(self):
        for _ in range(100):
            game_board = generator.create_permuted_board()
            result = solver.solve_sudoku(game_board, False)
            self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
