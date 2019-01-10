#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command-line Mastermind game, with AI."""
import curses
import logging
import random


# Color constants.
BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7

# Set up logging
logging.basicConfig(filename='mastermind.log', filemode='w', level=logging.DEBUG)


class Game(object):
    """Game information."""

    def __init__(self, scr, board):
        """Initialize the Game object on curses screen scr."""
        self.scr = scr
        self.board = board
        self.players = 1  # 1 -> single player, 2 -> two players

        # Initialize curses color pairs
        curses.init_pair(RED, RED, 0)
        curses.init_pair(GREEN, GREEN, 0)
        curses.init_pair(YELLOW, YELLOW, 0)
        curses.init_pair(BLUE, BLUE, 0)
        curses.init_pair(MAGENTA, MAGENTA, 0)
        curses.init_pair(CYAN, CYAN, 0)

    def draw_current_guess(self, window):
        """Draw the current guess code."""
        board = self.board
        guess = board.current_guess
        window.addstr("          ")
        for i in range(0, len(guess)):
            window.addstr("O", curses.color_pair(guess[i]))
            window.addstr("     ")
        for i in range(len(guess), 4):
            window.addstr("O")
            window.addstr("     ")
        window.addstr("\n")
    
    def draw_guess_list(self, window):
        """Draw the list of guesses, previous and to be made."""
        board = self.board
        guess_list = board.guess_history

        for i in range(0, len(guess_list)):
            pass  # TODO: Implement guess list
        for i in range(len(guess_list), 10):
            window.addstr("\n")

        window.addstr("\n\n")
    
    def draw_help_commands(self, window):
        """Draw the help command strings on the playing screen."""
        window.addstr("     Press ? to display the rules.\n")
        window.addstr("     Press n to start a new game.\n")
        window.addstr("     Press r to reset the guess.\n")
        window.addstr("     Press q to quit.")

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
            r" __  __         _                 _         _ ""\n"
            r"|  \/  |__ _ __| |_ ___ _ _ _ __ (_)_ _  __| |""\n"
            r"| |\/| / _` (_-<  _/ -_) '_| '  \| | ' \/ _` |""\n"
            r"|_|  |_\__,_/__/\__\___|_| |_|_|_|_|_||_\__,_|""\n"
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

        scr.clear()
        scr.addstr(0, 0, "mastermind.py", curses.A_REVERSE)
        scr.refresh()

        height, width = 20, 40
        max_y, max_x = scr.getmaxyx()
        text_window = curses.newwin(
            height,
            width,
            int((max_y - height)/2),
            int((max_x - width - 1)/2),  # ignore \n in calculation
        )

        text_window.clear()
        self.draw_select_color(text_window)
        self.draw_current_guess(text_window)
        self.draw_guess_list(text_window)
        self.draw_help_commands(text_window)

        text_window.refresh()

        curses.curs_set(0)
        self.playing_screen_keyloop()
    
    def draw_select_color(self, window):
        """Draw the "select color" text on window."""
        window.addstr("   Use ")
        window.addstr("a ", curses.color_pair(RED))
        window.addstr("s ", curses.color_pair(GREEN))
        window.addstr("d ", curses.color_pair(YELLOW))
        window.addstr("f ", curses.color_pair(BLUE))
        window.addstr("g ", curses.color_pair(MAGENTA))
        window.addstr("h ", curses.color_pair(CYAN))
        window.addstr("to select a color.  \n")
        window.addstr("\n")

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
        board = self.board
        key_colors = {
            'a': RED,
            's': GREEN,
            'd': YELLOW,
            'f': BLUE,
            'g': MAGENTA,
            'h': CYAN
        }

        valid_keys = {'a', 's', 'd', 'f', 'g', 'h', '?', 'n', 'r', 'q'}
        while True:
            key = scr.getkey().lower()
            while key not in valid_keys:
                key = scr.getkey().lower()

            if key in key_colors:
                try:
                    board.add_color(key_colors[key])
                    self.draw_playing_screen()
                except ValueError:
                    continue
            elif key == '?':
                pass # TODO: Implement help screen
            elif key == 'n':
                pass # TODO: Implement new game screen
            elif key == 'r':
                pass # TODO: Implement reset guess procedure
            elif key == 'q':  # Quit
                break

            break  # Exit from extra loop

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
            colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
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
        self.current_guess = []  # [colors...]
        self.guess_history = []  # [(guess, feedback)...]

    def add_color(self, color):
        """Append a color to the current guess."""
        current_guess = self.current_guess

        if not len(current_guess) < 4:
            raise ValueError("Can't pick more than 4 colors.")
        
        if color not in {RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN}:
            raise ValueError("Invalid color.")

        for current_guess_color in current_guess:
            if color == current_guess_color:
                raise ValueError("Cannot repeat colors in guess.")

        current_guess.append(color)

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

        self.guess_history.append((guess, feedback))

        return feedback


def main(stdscr):
    """Play the Mastermind game on curses screen stdscr."""
    board = Board()
    game = Game(stdscr, board)
    game.start()


if __name__ == '__main__':
    curses.wrapper(main)
