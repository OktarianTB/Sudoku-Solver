import unittest
import board, solver


class TestSolver(unittest.TestCase):

    def test_easy50(self):
        lines = board.get_lines("easy50.txt")
        if not lines:
            print("Wrong filename")
            return
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            result = solver.solve(game_board)
            self.assertEqual(result, True)

    def test_hardest(self):
        lines = board.get_lines("hardest.txt")
        if not lines:
            print("Wrong filename")
            return
        for line in lines:
            game_board = board.convert_str_to_2d_board(line.replace("\n", ""))
            result = solver.solve(game_board)
            self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()