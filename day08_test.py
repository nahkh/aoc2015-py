import unittest
from day08 import *


class TestDay8(unittest.TestCase):

    def test_character_counts(self):
        self.assertEqual(count_characters('""'), (2, 0))
        self.assertEqual(count_characters('"abc"'), (5, 3))
        self.assertEqual(count_characters('"\\x27"'), (6, 1))
        self.assertEqual(count_characters('"aaa\\\\aaa"'), (10, 7))
        self.assertEqual(count_characters('"aaa\\"aaa"'), (10, 7))

    def test_summary_difference(self):
        test_data = '""\n"abc"\n"\\x27"\n"aaa\\"aaa"'.splitlines()
        self.assertEqual(summary_difference(test_data), (23, 11, 12))


if __name__ == '__main__':
    unittest.main()
