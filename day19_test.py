import unittest
from day19 import *


class TestDay19(unittest.TestCase):

    def setUp(self):
        with open('input19_test.txt') as f:
            self.plant = MedicinePlant.parse(f.readlines())

    def test_count_distinct_replacements(self):
        self.assertEqual(7, self.plant.count_distinct_replacements())

    def test_search(self):
        self.assertEqual(6, self.plant.search())

    def test_reverse_search(self):
        self.assertEqual(6, self.plant.reverse_search(self.plant.medicine_molecule))


if __name__ == '__main__':
    unittest.main()
