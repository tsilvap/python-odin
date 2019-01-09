from mastermind import (
    BLACK, WHITE, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN,
    Board
)


def test_guess():
    """Test Board.guess method."""
    board = Board([RED, GREEN, CYAN, YELLOW], 100)

    # all correct
    assert board.guess([RED, GREEN, CYAN, YELLOW]) == [BLACK, BLACK, BLACK, BLACK]

    # three correct
    assert board.guess([RED, GREEN, CYAN, BLUE]) == [BLACK, BLACK, BLACK]

    # two correct, two swapped
    assert board.guess([RED, CYAN, GREEN, YELLOW]) == [BLACK, BLACK, WHITE, WHITE]

    # two correct, one swapped
    assert board.guess([RED, CYAN, MAGENTA, YELLOW]) == [BLACK, BLACK, WHITE]

    # two correct
    assert board.guess([RED, GREEN, MAGENTA, BLUE]) == [BLACK, BLACK]

    # one correct, three swapped
    assert board.guess([GREEN, YELLOW, CYAN, RED]) == [BLACK, WHITE, WHITE, WHITE]

    # one correct, two swapped
    assert board.guess([GREEN, YELLOW, CYAN, MAGENTA]) == [BLACK, WHITE, WHITE]

    # one correct, one swapped
    assert board.guess([GREEN, BLUE, CYAN, MAGENTA]) == [BLACK, WHITE]

    # four swapped
    assert board.guess([YELLOW, RED, GREEN, CYAN]) == [WHITE, WHITE, WHITE, WHITE]

    # three swapped
    assert board.guess([BLUE, RED, GREEN, CYAN]) == [WHITE, WHITE, WHITE]

    # two swapped
    assert board.guess([BLUE, RED, GREEN, MAGENTA]) == [WHITE, WHITE]
