import unittest
from stock_picker import stock_picker


class TestStockPicker(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(stock_picker([17, 3, 6, 9, 15, 8, 6, 1, 10]), [1, 4])

    def test_ascending(self):
        self.assertEqual(stock_picker([1, 2, 3, 4, 5]), [0, 4])

    def test_descending(self):
        self.assertEqual(stock_picker([5, 4, 3, 2, 1]), [])

    def test_lowest_last(self):
        self.assertEqual(stock_picker([5, 3, 4, 7, 1]), [1, 3])

    def test_highest_first(self):
        self.assertEqual(stock_picker([7, 1, 3, 1, 5, 4]), [1, 4])

    def test_all_equal(self):
        self.assertEqual(stock_picker([4, 4, 4, 4, 4, 4, 4]), [])

    def test_one_day(self):
        self.assertEqual(stock_picker([12]), [])

    def test_zero_days(self):
        self.assertEqual(stock_picker([]), [])


if __name__ == "__main__":
    unittest.main()
