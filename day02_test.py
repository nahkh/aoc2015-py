import unittest
from day02 import *


class TestDay2(unittest.TestCase):

    def test_parse_box_dimensions(self):
        self.assertEqual(Package.parse("7x8x2"), Package(7, 8, 2))
        self.assertEqual(Package.parse("700x821234x214"), Package(700, 821234, 214))

    def test_calculate_needed_wrapping_paper(self):
        self.assertEqual(Package(2, 3, 4).needed_wrapping_paper(), 58)
        self.assertEqual(Package(1, 1, 10).needed_wrapping_paper(), 43)

    def test_calculate_needed_ribbon(self):
        self.assertEqual(Package(2, 3, 4).needed_ribbon(), 34)
        self.assertEqual(Package(1, 1, 10).needed_ribbon(), 14)


if __name__ == '__main__':
    unittest.main()
