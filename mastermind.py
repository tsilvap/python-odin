#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command-line Mastermind game, with AI."""
import curses
import random


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

    def __init__(self, scr, board):
        """Initialize the Game object on curses screen scr."""
        self.scr = scr
        self.board = board
        self.players = 1  # 1 -> single player, 2 -> two players

    def draw_text_centralized(self, text, height, width):
        """Draw text in a centralized window (height, width)."""
        scr = self.scr

        max_y, max_x = scr.getmaxyx()
        text_window = curses.newwin(
            height,
            width,
            int((max_y - height)/2),
            int((max_x - width - 1)/2),  # ignore \n in calculation
        )
        text_window.addstr(text)
        text_window.refresh()

    def draw_initial_screen(self, players=None):
        """Draw the initial screen."""
        if players is not None:
            self.players = players

        scr = self.scr
        scr.addstr(0, 0, "mastermind.py", curses.A_REVERSE)
        scr.refresh()

        logo = (
            " __  __         _                 _         _ \n"
            "|  \/  |__ _ __| |_ ___ _ _ _ __ (_)_ _  __| |\n"
            "| |\/| / _` (_-<  _/ -_) '_| '  \| | ' \/ _` |\n"
            "|_|  |_\__,_/__/\__\___|_| |_|_|_|_|_||_\__,_|\n"
            "                                              \n"
            "                                              \n"
        )
        modes = (
            "              > 1P vs computer                \n"
            "                1P vs 2P                      \n"
            if self.players == 1 else
            "                1P vs computer                \n"
            "              > 1P vs 2P                      \n"
        )
        instructions = (
            "                                              \n"
            "                                              \n"
            "    Press s to select and start the game.     \n"
        )
        initial_text = logo + modes + instructions
        height = 12  # text height
        width = 47  # text width (including \n)

        self.draw_text_centralized(initial_text, height, width)

        curses.curs_set(0)
        self.initial_screen_keyloop()

    def draw_playing_screen(self, players=1):
        """Draw the playing screen."""
        scr = self.scr

        if players == 1:
            scr.addstr(0, 0, "mastermind.py", curses.A_REVERSE)

            select_colors = (
                "   Use a s d f g h to select a color.  \n"
                "                                       \n"
                "          O     O     O     O          \n"
            )
            
            height = 18
            width = 40

            self.draw_text_centralized(select_colors, height, width)

            curses.curs_set(0)
            self.playing_screen_keyloop()

        else:
            pass  # TODO: Implement 2-player mode


    def initial_screen_keyloop(self):
        """The initial screen keyloop."""
        scr = self.scr

        key = scr.getch()
        while key not in {curses.KEY_DOWN, curses.KEY_UP, ord('s'), ord('S')}:
            key = scr.getch()

        if key in {curses.KEY_DOWN, curses.KEY_UP}:
            self.draw_initial_screen(2 if self.players == 1 else 1)

        else:  # Start the game
            pass  # TODO: Implement this.

    def playing_screen_keyloop(self):
        """The playing screen keyloop"""
        scr = self.scr

        key = scr.getch()

    def start(self):
        """Start the game and execute its lifecycle."""
        self.draw_initial_screen()
        self.draw_playing_screen()


class Board(object):
    """Mastermind board information."""

    def __init__(self, code=None, tries=10):
        """Initialize the board.

        :param code: List of four colors, the code to be cracked.
        :param tries: Maximum number of tries to crack the code.
        """
        if code is None:
            # Generate a random code
            colors = [RED, GREEN, YELLOW, BLUE, VIOLET, CYAN]
            code = []
            for i in range(0, 4):
                color_index = random.randrange(0, len(colors))
                code.append(colors[color_index])
                colors.pop(color_index)
            self.code = code
        else:
            # Use code provided as a parameter
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
    board = Board()
    game = Game(stdscr, board)
    game.start()


if __name__ == '__main__':
    curses.wrapper(main)
