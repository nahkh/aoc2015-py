import unittest
from day12 import *


class TestDay12(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers('[1,2,3]'), 6)
        self.assertEqual(sum_numbers('{"a":2,"b":4}'), 6)
        self.assertEqual(sum_numbers('[[[3]]]'), 3)
        self.assertEqual(sum_numbers('{"a":{"b":4},"c":-1}'), 3)
        self.assertEqual(sum_numbers('{"a":[-1,1]}'), 0)
        self.assertEqual(sum_numbers('[-1,{"a":1}]'), 0)
        self.assertEqual(sum_numbers('[]'), 0)
        self.assertEqual(sum_numbers('{}'), 0)


if __name__ == '__main__':
    unittest.main()
