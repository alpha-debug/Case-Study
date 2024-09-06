import unittest
from tictactoe import print_board, check_winner, tic_tac_toe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def test_print_board(self):
        # This test is more about visual inspection since print_board prints to console
        print_board(self.board)

    def test_check_winner_horizontal(self):
        self.board[0] = ["X", "X", "X"]
        self.assertTrue(check_winner(self.board, "X"))

    def test_check_winner_vertical(self):
        for i in range(3):
            self.board[i][0] = "O"
        self.assertTrue(check_winner(self.board, "O"))

    def test_check_winner_diagonal(self):
        for i in range(3):
            self.board[i][i] = "X"
        self.assertTrue(check_winner(self.board, "X"))

    def test_no_winner(self):
        self.assertFalse(check_winner(self.board, "X"))
        self.assertFalse(check_winner(self.board, "O"))

if __name__ == '__main__':
    unittest.main()
