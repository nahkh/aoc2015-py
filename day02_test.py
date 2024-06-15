import unittest
from day02 import *


class TestDay1(unittest.TestCase):

    def test_parse_box_dimensions(self):
        self.assertEqual(parse_box_dimensions("7x8x2"), (7, 8, 2))
        self.assertEqual(parse_box_dimensions("700x821234x214"), (700, 821234, 214))

    def test_calculate_needed_wrapping_paper(self):
        self.assertEqual(calculate_needed_wrapping_paper((2, 3, 4)), 58)
        self.assertEqual(calculate_needed_wrapping_paper((1, 1, 10)), 43)


if __name__ == '__main__':
    unittest.main()
