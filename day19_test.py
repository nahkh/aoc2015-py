import unittest
from day19 import *


class TestDay19(unittest.TestCase):

    def setUp(self):
        with open('input19_test.txt') as f:
            self.plant = MedicinePlant.parse(f.readlines())

    def test_count_distinct_replacements(self):
        self.assertEqual(7, self.plant.count_distinct_replacements())


if __name__ == '__main__':
    unittest.main()
