#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command-line Mastermind game, with AI."""
import curses


# Color constants.
BLACK = 0
WHITE = 1
RED = 2
GREEN = 3
YELLOW = 4
BLUE = 5
VIOLET = 6
CYAN = 7


class Game(object):
    """Game information."""

    def __init__(self, scr):
        """Initialize the Game object on curses screen scr."""
        self.scr = scr

    def draw_initial_screen(self):
        """Draw the initial screen."""
        scr = self.scr
        scr.addstr(0, 0, "mastermind.py", curses.A_REVERSE)
        scr.refresh()

        initial_text = (
            " __  __         _                 _         _ \n"
            "|  \/  |__ _ __| |_ ___ _ _ _ __ (_)_ _  __| |\n"
            "| |\/| / _` (_-<  _/ -_) '_| '  \| | ' \/ _` |\n"
            "|_|  |_\__,_/__/\__\___|_| |_|_|_|_|_||_\__,_|\n"
            "                                              \n"
            "                                              \n"
            "              > 1P vs computer                \n"
            "                1P vs 2P                      \n"
        )
        text_height = 9
        text_width = 47

        max_y, max_x = scr.getmaxyx()
        text_window = curses.newwin(
            text_height,
            text_width,
            int((max_y - text_height)/2),
            int((max_x - text_width - 1)/2),  # ignore \n in calculation
        )
        text_window.addstr(initial_text)
        text_window.refresh()

        curses.curs_set(0)
        scr.getkey()



class Board(object):
    """Mastermind board information."""

    def __init__(self, code=None, tries=10):
        """Initialize the board.

        :param code: List of four colors, the code to be cracked.
        :param tries: Maximum number of tries to crack the code.
        """
        self.code = code
        self.tries = tries

    def guess(self, guess):
        """Guess a combination of colors.

        :param guess: List of four colors, the guess combination.
        :return feedback: A list of black and white colors, indicating
        how good the guess was. Each black color element indicates
        there's a right color in the right spot, and each white element
        indicates there's a right color in the wrong spot. Is None if
        there are no tries left.
        """
        if self.tries < 1:
            return None
        else:
            self.tries -= 1

        feedback = []

        # Extract correct colors in the right spot
        remaining_guess = guess.copy()
        for i in range(0, len(guess)):
            if guess[i] == self.code[i]:
                feedback.append(BLACK)
                remaining_guess.remove(guess[i])

        # Extract correct colors in the wrong spot
        for i in range(0, len(remaining_guess)):
            for j in range(0, len(self.code)):
                if remaining_guess[i] == self.code[j]:
                    feedback.append(WHITE)
                    break

        return feedback


def main(stdscr):
    """Play the Mastermind game on curses screen stdscr."""
    game = Game(stdscr)
    board = Board()
    game.draw_initial_screen()


if __name__ == '__main__':
    curses.wrapper(main)
