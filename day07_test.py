import unittest
from day07 import *


class TestDay7(unittest.TestCase):

    def test_evaluation(self):
        test_definition = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""
        eg = ExecutionGraph.create([Operation.parse(line) for line in test_definition.splitlines()])
        eg.evaluate_all()
        self.assertEqual(eg.computed_values, {
            'd': 72,
            'e': 507,
            'f': 492,
            'g': 114,
            'h': 65412,
            'i': 65079,
            'x': 123,
            'y': 456})


if __name__ == '__main__':
    unittest.main()
