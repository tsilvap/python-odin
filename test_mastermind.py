from mastermind import (
    BLACK, WHITE, RED, GREEN, YELLOW, BLUE, VIOLET, CYAN,
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
    assert board.guess([RED, CYAN, VIOLET, YELLOW]) == [BLACK, BLACK, WHITE]

    # two correct
    assert board.guess([RED, GREEN, VIOLET, BLUE]) == [BLACK, BLACK]

    # one correct, three swapped
    assert board.guess([GREEN, YELLOW, CYAN, RED]) == [BLACK, WHITE, WHITE, WHITE]

    # one correct, two swapped
    assert board.guess([GREEN, YELLOW, CYAN, VIOLET]) == [BLACK, WHITE, WHITE]

    # one correct, one swapped
    assert board.guess([GREEN, BLUE, CYAN, VIOLET]) == [BLACK, WHITE]

    # four swapped
    assert board.guess([YELLOW, RED, GREEN, CYAN]) == [WHITE, WHITE, WHITE, WHITE]

    # three swapped
    assert board.guess([BLUE, RED, GREEN, CYAN]) == [WHITE, WHITE, WHITE]

    # two swapped
    assert board.guess([BLUE, RED, GREEN, VIOLET]) == [WHITE, WHITE]
