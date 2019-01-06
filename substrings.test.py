import unittest
from substrings import substrings


class TestSubstrings(unittest.TestCase):
    def setUp(self):
        self.dictionary = [
            "below",
            "down",
            "go",
            "going",
            "horn",
            "how",
            "howdy",
            "it",
            "i",
            "low",
            "own",
            "part",
            "partner",
            "sit",
        ]

    def test_word(self):
        self.assertEqual(
            substrings("below", self.dictionary), {"below": 1, "low": 1}
        )

    def test_sentence(self):
        self.assertEqual(
            substrings(
                "Howdy partner, sit down! How's it going?", self.dictionary
            ),
            {
                "down": 1,
                "how": 2,
                "howdy": 1,
                "go": 1,
                "going": 1,
                "it": 2,
                "i": 3,
                "own": 1,
                "part": 1,
                "partner": 1,
                "sit": 1,
            },
        )

    def test_one_word(self):
        self.assertEqual(substrings("partn", self.dictionary), {"part": 1})

    def test_no_words(self):
        self.assertEqual(substrings("ayyy", self.dictionary), {})


if __name__ == "__main__":
    unittest.main()
