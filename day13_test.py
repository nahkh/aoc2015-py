import unittest
from day13 import *


class TestDay13(unittest.TestCase):
    def setUp(self) -> None:
        with open("input13_test.txt") as f:
            self.table = Table.parse(f.readlines())

    def test_evaluate_ordering(self):
        self.assertEqual(self.table.evaluate_ordering(['Alice', 'Bob', 'Carol', 'David']), 330)

    def test_find_max_ordering(self):
        self.assertEqual(self.table.find_max_ordering(), (('Alice', 'Bob', 'Carol', 'David'), 330))


if __name__ == '__main__':
    unittest.main()
