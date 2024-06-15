import unittest
from day05 import *


class TestDay5(unittest.TestCase):

    def test_is_really_nice(self):
        self.assertTrue(is_really_nice("qjhvhtzxzqqjkmpb"))
        self.assertTrue(is_really_nice("xxyxx"))
        self.assertFalse(is_really_nice("uurcxstgmygtbstg"))
        self.assertFalse(is_really_nice("ieodomkazucvgmuy"))
        self.assertTrue(line_contains_any_two_pairs("uurcxstgmygtbstg"))
        self.assertFalse(contains_two_consecutive_characters_separated_by_one("uurcxstgmygtbstg"))
        self.assertTrue(contains_two_consecutive_characters_separated_by_one("ieodomkazucvgmuy"))
        self.assertFalse(line_contains_any_two_pairs("ieodomkazucvgmuy"))



if __name__ == '__main__':
    unittest.main()
