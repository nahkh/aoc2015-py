import unittest
from day14 import *


class TestDay14(unittest.TestCase):

    def test_distance_traveled(self):
        comet = Reindeer.parse('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.')
        self.assertEqual(comet.distance_traveled(1000), 1120)
        dancer = Reindeer.parse('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
        self.assertEqual(dancer.distance_traveled(1000), 1056)


if __name__ == '__main__':
    unittest.main()
