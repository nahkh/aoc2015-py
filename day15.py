from __future__ import annotations
import dataclasses
from enum import Enum
import itertools
import re
from typing import Tuple, Dict, List, Generator

INGREDIENT_PATTERN = re.compile(
    r'^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')


class IngredientProperty(Enum):
    CAPACITY = 1
    DURABILITY = 2
    FLAVOR = 3
    TEXTURE = 4
    CALORIES = 5

    @classmethod
    def score_values(cls) -> Generator[IngredientProperty]:
        yield IngredientProperty.CAPACITY
        yield IngredientProperty.DURABILITY
        yield IngredientProperty.FLAVOR
        yield IngredientProperty.TEXTURE

@dataclasses.dataclass(frozen=True)
class IngredientPropertyMap:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __getitem__(self, item: IngredientProperty) -> int:
        assert isinstance(item, IngredientProperty)
        if item == IngredientProperty.CAPACITY:
            return self.capacity
        elif item == IngredientProperty.DURABILITY:
            return self.durability
        elif item == IngredientProperty.FLAVOR:
            return self.flavor
        elif item == IngredientProperty.TEXTURE:
            return self.texture
        elif item == IngredientProperty.CALORIES:
            return self.calories
        else:
            assert False, f'Unhandled ingredient property {item}'


@dataclasses.dataclass(frozen=True)
class Ingredient:
    name: str
    properties: IngredientPropertyMap

    @classmethod
    def parse(cls, line: str) -> Ingredient:
        m = INGREDIENT_PATTERN.match(line)
        assert m, f'"{line}" did not match the expected pattern'
        name = m.group(1)
        capacity = int(m.group(2))
        durability = int(m.group(3))
        flavor = int(m.group(4))
        texture = int(m.group(5))
        calories = int(m.group(6))
        return Ingredient(name, IngredientPropertyMap(capacity, durability, flavor, texture, calories))


@dataclasses.dataclass(frozen=True)
class IngredientList:
    ingredients: Tuple[Ingredient]

    @classmethod
    def parse(cls, lines: List[str]) -> IngredientList:
        return IngredientList(tuple(Ingredient.parse(line) for line in lines))

    def all_possible_recipes(self, remaining_volume: int = 100, used_ingredients: Dict[Ingredient, int]=None) -> Generator[Recipe]:
        if not used_ingredients:
            used_ingredients = {}
        if remaining_volume == 0:
            yield Recipe(used_ingredients)
            return
        remaining_possible_ingredients = set(self.ingredients).difference(used_ingredients.keys())
        assert remaining_possible_ingredients, 'Unexpected end of ingredient list'
        if len(remaining_possible_ingredients) == 1:
            ingredient = next(iter(remaining_possible_ingredients))
            used_ingredients = dict(used_ingredients)
            used_ingredients[ingredient] = remaining_volume
            yield Recipe(used_ingredients)
            return
        else:
            ingredient = next(iter(remaining_possible_ingredients))
            for i in range(0, remaining_volume + 1):
                new_used_ingredients = dict(used_ingredients)
                new_used_ingredients[ingredient] = i
                for recipe in self.all_possible_recipes(remaining_volume - i, new_used_ingredients):
                    yield recipe

    def find_best_recipe(self) -> Recipe:
        best_recipe = None
        best_score = 0
        for recipe in self.all_possible_recipes():
            score = recipe.score()
            if not best_recipe or best_score < score:
                best_score = score
                best_recipe = recipe
        return best_recipe


@dataclasses.dataclass(frozen=True)
class Recipe:
    ingredients: Dict[Ingredient, int]

    def score(self) -> int:
        score = 1
        for ingredient_property in IngredientProperty.score_values():
            property_score = 0
            for ingredient, amount in self.ingredients.items():
                property_score += ingredient.properties[ingredient_property] * amount
            if property_score < 0:
                property_score = 0
            score *= property_score
        return score


def part1(ingredient_list: IngredientList):
    print(f'Day 15, part 1: The best score achievable is {ingredient_list.find_best_recipe().score()}')


def main():
    with open('input15.txt') as f:
        ingredient_list = IngredientList.parse(f.readlines())
        part1(ingredient_list)


if __name__ == '__main__':
    main()
