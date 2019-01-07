import random
from curses import wrapper


class Game:
    def __init__(self, scr):
        self.scr = scr

    def draw(self, board, finished=False, winner=None):
        mark_0 = self.draw_mark(board.getMark(0))
        mark_1 = self.draw_mark(board.getMark(1))
        mark_2 = self.draw_mark(board.getMark(2))
        mark_3 = self.draw_mark(board.getMark(3))
        mark_4 = self.draw_mark(board.getMark(4))
        mark_5 = self.draw_mark(board.getMark(5))
        mark_6 = self.draw_mark(board.getMark(6))
        mark_7 = self.draw_mark(board.getMark(7))
        mark_8 = self.draw_mark(board.getMark(8))
        player = board.getPlayer()

        self.scr.clear()
        self.scr.addstr("\n")
        self.scr.addstr(f"  {mark_0} | {mark_1} | {mark_2}   ")
        if not finished:
            self.scr.addstr(f"You're player: {player}\n")
        elif winner:
            self.scr.addstr(f"Winner: {winner}\n")
        else:
            self.scr.addstr("Draw!\n")
        self.scr.addstr(" ---|---|---  ")
        if not finished:
            self.scr.addstr("Press one of the keys below to place a mark.\n")
        else:
            self.scr.addstr("Press q to quit, or n to start a new game.\n")
        self.scr.addstr(f"  {mark_3} | {mark_4} | {mark_5}   ")
        if not finished:
            self.scr.addstr("q w e\n")
        else:
            self.scr.addstr("\n")
        self.scr.addstr(" ---|---|---  ")
        if not finished:
            self.scr.addstr("a s d\n")
        else:
            self.scr.addstr("\n")
        self.scr.addstr(f"  {mark_6} | {mark_7} | {mark_8}   ")
        if not finished:
            self.scr.addstr("z x c\n")
        else:
            self.scr.addstr("\n")
        self.scr.refresh()


    def draw_mark(self, mark):
        if mark in {'O', 'X'}:
            return mark

        return ' '
    
    def start(self, board):
        while not board.isFinished():
            self.draw(board)
            positions = {
                'q': 0, 'w': 1, 'e': 2,
                'a': 3, 's': 4, 'd': 5,
                'z': 6, 'x': 7, 'c': 8
            }
            key = self.scr.getkey().lower()
            while key not in positions:
                key = self.scr.getkey()
            board.placeMark(positions[key])

        self.draw(board, finished=True, winner=board.getWinner())
        key = self.scr.getkey()
        while key not in {'Q', 'q', 'N', 'n'}:
            key = self.scr.getkey()

        if key in {'N', 'n'}:
            board = Board()
            self.start(board)


class Board:
    def __init__(self):
        self.state = [
            None, None, None,
            None, None, None,
            None, None, None
        ]
        self.winner = None
        self.player = 'X' if random.randint(0, 1) else 'O'

    def getMark(self, position):
        return self.state[position]

    def getPlayer(self):
        return self.player

    def getWinner(self):
        """Return mark of board's winner, if there is one, else None."""
        if self.isFinished():
            return self.winner

        return None
    
    def isFinished(self):
        """Return whether the game is finished."""
        lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        is_board_filled = True

        # If there is a winner, return True
        for line in lines:
            first_mark = self.getMark(line[0])
            if first_mark is not None:
                is_winner = True
                for position in line:
                    mark = self.getMark(position)
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

    def placeMark(self, position):
        """Place a mark at position, if the square is empty."""
        if not self.state[position]:
            self.state[position] = self.player
            if self.player == 'O':
                self.player = 'X'
            elif self.player == 'X':
                self.player = 'O'


def main(stdscr):
    game = Game(stdscr)
    board = Board()

    game.start(board)


if __name__ == '__main__':
    wrapper(main)
