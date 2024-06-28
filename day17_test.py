import unittest
from day17 import *


class TestDay17(unittest.TestCase):

    def test_count_possible_ways_to_reach_sum(self):
        self.assertEqual(count_possible_ways_to_reach_sum(25, (20, 15, 10, 5, 5)), 4)


if __name__ == '__main__':
    unittest.main()
