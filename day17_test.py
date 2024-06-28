import unittest
from day17 import *


class TestDay17(unittest.TestCase):

    def test_count_possible_ways_to_reach_sum(self):
        self.assertEqual(4, count_possible_ways_to_reach_sum(25, (20, 15, 10, 5, 5)))

    def test_find_minimum_number_of_containers(self):
        self.assertEqual(2, find_minimum_number_of_containers(25, (20, 15, 10, 5, 5), 0))

    def test_count_possible_ways_to_reach_sum_with_n_containers(self):
        self.assertEqual(3, count_possible_ways_to_reach_sum_with_n_containers(25, (20, 15, 10, 5, 5), 2))


if __name__ == '__main__':
    unittest.main()
