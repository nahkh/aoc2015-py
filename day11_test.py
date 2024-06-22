import unittest
from day11 import *


class TestDay11(unittest.TestCase):

    def test_next_candidate(self):
        self.assertEqual(next_candidate('xx'), 'xy')
        self.assertEqual(next_candidate('xy'), 'xz')
        self.assertEqual(next_candidate('xz'), 'ya')
        self.assertEqual(next_candidate('zzzzz'), 'aaaaa')

    def test_password_is_valid(self):
        self.assertEqual(password_is_valid('hijklmmn'), False)
        self.assertEqual(password_is_valid('abbceffg'), False)
        self.assertEqual(password_is_valid('abbcegjk'), False)

    def test_straights(self):
        straights = get_straights()
        self.assertIn('abc', straights)
        self.assertIn('xyz', straights)
        self.assertEqual(len(straights), 24)

    def test_find_next_valid_password(self):
        self.assertEqual(find_next_valid_password('abcdefgh'), 'abcdffaa')
        self.assertEqual(find_next_valid_password('ghijklmn'), 'ghjaabcc')


if __name__ == '__main__':
    unittest.main()
