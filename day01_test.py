import unittest
import day01


class TestDay1(unittest.TestCase):

    def test_calculate_reached_floor(self):
        self.assertEqual(day01.calculate_reached_floor("(())"), 0)
        self.assertEqual(day01.calculate_reached_floor("()()"), 0)
        self.assertEqual(day01.calculate_reached_floor("((("), 3)
        self.assertEqual(day01.calculate_reached_floor("(()(()("), 3)
        self.assertEqual(day01.calculate_reached_floor("))((((("), 3)
        self.assertEqual(day01.calculate_reached_floor("())"), -1)
        self.assertEqual(day01.calculate_reached_floor("))("), -1)
        self.assertEqual(day01.calculate_reached_floor(")))"), -3)
        self.assertEqual(day01.calculate_reached_floor(")())())"), -3)

    def test_calculate_first_basement_position(self):
        self.assertEqual(day01.calculate_first_basement_position(")"), 1)
        self.assertEqual(day01.calculate_first_basement_position("()())"), 5)


if __name__ == '__main__':
    unittest.main()
