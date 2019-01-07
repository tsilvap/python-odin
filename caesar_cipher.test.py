import unittest
from caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    def test_rot23_upper(self):
        self.assertEqual(
            caesar_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23),
            "XYZABCDEFGHIJKLMNOPQRSTUVW",
        )

    def test_rot23_spaces(self):
        self.assertEqual(
            caesar_cipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 23),
            "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD",
        )

    def test_rot13_symbol(self):
        self.assertEqual(caesar_cipher("What a string!", 5), "Bmfy f xywnsl!")

    def test_rot27_one_letter(self):
        self.assertEqual(caesar_cipher("A", 27), "B")

    def test_negative_shift(self):
        self.assertEqual(caesar_cipher("a", -2), "y")

    def test_no_letters(self):
        self.assertEqual(caesar_cipher("", 13), "")


if __name__ == "__main__":
    unittest.main()
