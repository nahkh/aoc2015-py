import unittest
from day15 import *


class TestDay15(unittest.TestCase):

    def setUp(self) -> None:
        with open("input15_test.txt") as f:
            self.ingredient_list = IngredientList.parse(f.readlines())

    def test_find_best_recipe(self):
        self.assertEqual(self.ingredient_list.find_best_recipe().score(), 62842880)


if __name__ == '__main__':
    unittest.main()
