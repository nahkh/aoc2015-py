import unittest
from day09 import *


class TestDay9(unittest.TestCase):

    def test_find_shortest_path(self):
        lines = '''London to Dublin = 464
        London to Belfast = 518
        Dublin to Belfast = 141
        '''.splitlines()
        graph = Graph.create(lines)
        print(graph)
        self.assertEqual(graph.find_shortest_path(), 605)


if __name__ == '__main__':
    unittest.main()
