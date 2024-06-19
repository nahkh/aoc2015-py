import unittest
from day10 import *


class TestDay10(unittest.TestCase):

    def test_iterate(self):
        self.assertEqual(iterate('1'), '11')
        self.assertEqual(iterate('11'), '21')
        self.assertEqual(iterate('21'), '1211')
        self.assertEqual(iterate('1211'), '111221')
        self.assertEqual(iterate('111221'), '312211')


if __name__ == '__main__':
    unittest.main()
