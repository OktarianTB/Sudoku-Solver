import unittest
import board, solver


class TestSolver(unittest.TestCase):

    def check(self, lines):
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            result = solver.solve(game_board)
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


if __name__ == "__main__":
    unittest.main()
