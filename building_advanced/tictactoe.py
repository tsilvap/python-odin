#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command-line Tic Tac Toe game using curses library."""
import random
from curses import wrapper


class Game(object):
    """Contain information on how to start and draw the game."""

    def __init__(self, scr):
        """Attach a Game object to curses screen scr."""
        self.scr = scr

    def draw(self, board, finished=False, winner=None):
        """Draw each frame of the game."""
        mark0 = self.draw_mark(board.get_mark(0))
        mark1 = self.draw_mark(board.get_mark(1))
        mark2 = self.draw_mark(board.get_mark(2))
        mark3 = self.draw_mark(board.get_mark(3))
        mark4 = self.draw_mark(board.get_mark(4))
        mark5 = self.draw_mark(board.get_mark(5))
        mark6 = self.draw_mark(board.get_mark(6))
        mark7 = self.draw_mark(board.get_mark(7))
        mark8 = self.draw_mark(board.get_mark(8))
        player = board.get_player()

        self.scr.clear()
        self.scr.addstr('\n')
        self.scr.addstr('  {0} | {1} | {2}   '.format(mark0, mark1, mark2))
        if not finished:
            self.scr.addstr("You're player: {player}\n".format(player=player))
        elif winner:
            self.scr.addstr('Winner: {winner}\n'.format(winner=winner))
        else:
            self.scr.addstr('Draw!\n')
        self.scr.addstr(' ---|---|---  ')
        if not finished:
            self.scr.addstr('Press one of the keys below to place a mark.\n')
        else:
            self.scr.addstr('Press q to quit, or n to start a new game.\n')
        self.scr.addstr('  {0} | {1} | {2}   '.format(mark3, mark4, mark5))
        if not finished:
            self.scr.addstr('q w e\n')
        else:
            self.scr.addstr('\n')
        self.scr.addstr(' ---|---|---  ')
        if not finished:
            self.scr.addstr('a s d\n')
        else:
            self.scr.addstr('\n')
        self.scr.addstr('  {0} | {1} | {2}   '.format(mark6, mark7, mark8))
        if not finished:
            self.scr.addstr('z x c\n')
        else:
            self.scr.addstr('\n')
        self.scr.refresh()

    def draw_mark(self, mark):
        """Draw a single board mark."""
        if mark in {'O', 'X'}:
            return mark

        return ' '

    def start(self, board):
        """Start the game."""
        while not board.is_finished():
            self.draw(board)
            positions = {
                'q': 0,
                'w': 1,
                'e': 2,
                'a': 3,
                's': 4,
                'd': 5,
                'z': 6,
                'x': 7,
                'c': 8,
            }
            key = self.scr.getkey().lower()
            while key not in positions:
                key = self.scr.getkey()
            board.place_mark(positions[key])

        self.draw(board, finished=True, winner=board.get_winner())
        key = self.scr.getkey()
        while key not in {'Q', 'q', 'N', 'n'}:
            key = self.scr.getkey()

        if key in {'N', 'n'}:
            board = Board()
            self.start(board)


class Board(object):
    """Contain information on the game board."""

    def __init__(self):
        """Initialize the board.

        The board starts without marks and no winners. Randomize
        wether the first player starts with "X" or "O".
        """
        self.state = [None, None, None, None, None, None, None, None, None]
        self.winner = None
        self.player = 'X' if random.randint(0, 1) else 'O'

    def get_mark(self, position):
        """Return mark at position."""
        return self.state[position]

    def get_player(self):
        """Get this turn's player ("X" or "O")."""
        return self.player

    def get_winner(self):
        """Return mark of board's winner, if there is one, else None."""
        if self.is_finished():
            return self.winner

        return None

    def is_finished(self):
        """Return whether the game is finished."""
        lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        is_board_filled = True

        # If there is a winner, return True
        for line in lines:
            first_mark = self.get_mark(line[0])
            if first_mark is not None:
                is_winner = True
                for position in line:
                    mark = self.get_mark(position)
                    if mark is None:
                        is_board_filled = False
                    if mark != first_mark:
                        is_winner = False
                if is_winner:
                    self.winner = first_mark
                    return True
            else:
                is_board_filled = False

        return is_board_filled

    def place_mark(self, position):
        """Place a mark at position, if the square is empty."""
        if not self.state[position]:
            self.state[position] = self.player
            if self.player == 'O':
                self.player = 'X'
            elif self.player == 'X':
                self.player = 'O'


def main(stdscr):
    """Play a Tic Tac Toe game."""
    game = Game(stdscr)
    board = Board()

    game.start(board)


if __name__ == '__main__':
    wrapper(main)
