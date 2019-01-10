import unittest
from tictactoe import Game, Board


class TestIsFinished(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_winner_horizontal(self):
        self.board.state = [
            'X', None, 'X',
            None, 'X', None,
            'O', 'O', 'O'
        ]
        self.assertTrue(self.board.isFinished())

    def test_winner_vertical(self):
        self.board.state = [
            None, 'X', 'O',
            'O', 'X', None,
            None, 'X', None
        ]
        self.assertTrue(self.board.isFinished())

    def test_winner_diagonal(self):
        self.board.state = [
            'X', None, 'O',
            None, 'O', 'X',
            'O', None, 'X'
        ]
        self.assertTrue(self.board.isFinished())

    def test_no_winners(self):
        self.board.state = [
            'X', None, 'O',
            'O', 'O', 'X',
            'X', None, 'O'
        ]
        self.assertFalse(self.board.isFinished())

    def test_board_filled(self):
        self.board.state = [
            'X', 'O', 'X',
            'X', 'X', 'O',
            'O', 'X', 'O'
        ]
        self.assertTrue(self.board.isFinished())

    def test_board_empty(self):
        self.assertFalse(self.board.isFinished())


class TestGetWinner(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_winner_horizontal(self):
        self.board.state = [
            'X', None, 'X',
            None, 'X', None,
            'O', 'O', 'O'
        ]
        self.assertEqual(self.board.getWinner(), 'O')

    def test_winner_vertical(self):
        self.board.state = [
            None, 'X', 'O',
            'O', 'X', None,
            None, 'X', None
        ]
        self.assertEqual(self.board.getWinner(), 'X')

    def test_winner_diagonal(self):
        self.board.state = [
            'X', None, 'O',
            None, 'O', 'X',
            'O', None, 'X'
        ]
        self.assertEqual(self.board.getWinner(), 'O')

    def test_no_winners(self):
        self.board.state = [
            'X', None, 'O',
            'O', 'O', 'X',
            'X', None, 'O'
        ]
        self.assertIsNone(self.board.getWinner())

    def test_board_filled(self):
        self.board.state = [
            'X', 'O', 'X',
            'X', 'X', 'O',
            'O', 'X', 'O'
        ]
        self.assertIsNone(self.board.getWinner())

    def test_board_empty(self):
        self.assertIsNone(self.board.getWinner())


if __name__ == '__main__':
    unittest.main()
