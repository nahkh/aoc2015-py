import unittest
from day18 import *


class TestDay18(unittest.TestCase):

    def test_iteration(self):
        initial_state = GridState.parse(['##.#.#',
                                         '...##.',
                                         '#....#',
                                         '..#...',
                                         '#.#..#',
                                         '####.#'])
        next_state = initial_state.set_always_on_lights(initial_state.corners()).iterate()
        self.assertEqual(['#.##.#',
                          '####.#',
                          '...##.',
                          '......',
                          '#...#.',
                          '#.####'], next_state.render().splitlines())


if __name__ == '__main__':
    unittest.main()
