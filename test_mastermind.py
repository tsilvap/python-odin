import pytest
from mastermind import (
    BLACK,
    WHITE,
    RED,
    GREEN,
    YELLOW,
    BLUE,
    MAGENTA,
    CYAN,
    Board,
)


def test_guess():
    """Test Board.guess method."""
    board = Board([RED, GREEN, CYAN, YELLOW], 100)

    # All correct
    assert board.guess([RED, GREEN, CYAN, YELLOW]) == [
        BLACK,
        BLACK,
        BLACK,
        BLACK,
    ]

    # Three correct
    assert board.guess([RED, GREEN, CYAN, BLUE]) == [BLACK, BLACK, BLACK]

    # Two correct, two swapped
    assert board.guess([RED, CYAN, GREEN, YELLOW]) == [
        BLACK,
        BLACK,
        WHITE,
        WHITE,
    ]

    # Two correct, one swapped
    assert board.guess([RED, CYAN, MAGENTA, YELLOW]) == [BLACK, BLACK, WHITE]

    # Two correct
    assert board.guess([RED, GREEN, MAGENTA, BLUE]) == [BLACK, BLACK]

    # One correct, three swapped
    assert board.guess([GREEN, YELLOW, CYAN, RED]) == [
        BLACK,
        WHITE,
        WHITE,
        WHITE,
    ]

    # One correct, two swapped
    assert board.guess([GREEN, YELLOW, CYAN, MAGENTA]) == [BLACK, WHITE, WHITE]

    # One correct, one swapped
    assert board.guess([GREEN, BLUE, CYAN, MAGENTA]) == [BLACK, WHITE]

    # Four swapped
    assert board.guess([YELLOW, RED, GREEN, CYAN]) == [
        WHITE,
        WHITE,
        WHITE,
        WHITE,
    ]

    # Three swapped
    assert board.guess([BLUE, RED, GREEN, CYAN]) == [WHITE, WHITE, WHITE]

    # Two swapped
    assert board.guess([BLUE, RED, GREEN, MAGENTA]) == [WHITE, WHITE]


def test_add_color():
    """Test Board.add_color method"""
    board = Board()

    # Add one color
    board.add_color(RED)
    assert board.current_guess == [RED]

    # Add three more colors
    board.add_color(GREEN)
    board.add_color(CYAN)
    board.add_color(YELLOW)
    assert board.current_guess == [RED, GREEN, CYAN, YELLOW]

    # Add one more color, should throw error
    with pytest.raises(ValueError):
        board.add_color(BLUE)

    # Adding invalid color should also throw error
    board.current_guess = []
    with pytest.raises(ValueError):
        board.add_color('invalid')

    # Adding repeated colors should throw error
    board.current_guess = []
    board.add_color(RED)
    with pytest.raises(ValueError):
        board.add_color(RED)
