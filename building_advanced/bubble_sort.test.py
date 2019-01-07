import unittest
from bubble_sort import bubble_sort, bubble_sort_by


class TestBubbleSort(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(bubble_sort([4, 3, 78, 2, 0, 2]), [0, 2, 2, 3, 4, 78])

    def test_ascending(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 9, 21]), [1, 2, 3, 4, 9, 21])

    def test_descending(self):
        self.assertEqual(bubble_sort([21, 9, 4, 3, 2, 1]), [1, 2, 3, 4, 9, 21])

    def test_repeating(self):
        self.assertEqual(bubble_sort([7, 7, 7, 7]), [7, 7, 7, 7])

    def test_large_descending(self):
        self.assertEqual(
            bubble_sort([i for i in range(1000, -1, -1)]),
            [i for i in range(0, 1001)]
        )

    def test_one_element(self):
        self.assertEqual(bubble_sort([2]), [2])

    def test_no_elements(self):
        self.assertEqual(bubble_sort([]), [])


class TestBubbleSortBy(unittest.TestCase):
    def test_length(self):
        self.assertEqual(
            bubble_sort_by(
                ['hi', 'hello', 'hey'],
                lambda left, right: len(left) > len(right)
            ),
            ['hi', 'hey', 'hello']
        )

    def test_alphabetical(self):
        self.assertEqual(
            bubble_sort_by(
                ['beatiful', 'is', 'better', 'than', 'ugly'],
                lambda left, right: left > right
            ),
            ['beatiful', 'better', 'is', 'than', 'ugly']
        )


if __name__ == '__main__':
    unittest.main()
