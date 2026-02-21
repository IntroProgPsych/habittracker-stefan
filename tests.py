# tests.py

import unittest
from app import interpret_score


class TestInterpretScore(unittest.TestCase):

    def test_high_score(self):
        self.assertEqual(interpret_score(12), "High")
        self.assertEqual(interpret_score(20), "High")

    def test_moderate_score(self):
        self.assertEqual(interpret_score(6), "Moderate")
        self.assertEqual(interpret_score(10), "Moderate")
        self.assertEqual(interpret_score(11), "Moderate")

    def test_low_score(self):
        self.assertEqual(interpret_score(0), "Low")
        self.assertEqual(interpret_score(5), "Low")


if __name__ == "__main__":
    unittest.main()
