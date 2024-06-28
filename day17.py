from __future__ import annotations
from functools import cache
from typing import Tuple


@cache
def count_possible_ways_to_reach_sum(target: int, values: Tuple[int]) -> int:
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return 1 if target == values[0] else 0
    possible_ways = 0
    next_values = tuple(list(values)[1:])
    if values[0] == target:
        possible_ways += 1
    elif values[0] < target:
        possible_ways += count_possible_ways_to_reach_sum(target - values[0], next_values)
    possible_ways += count_possible_ways_to_reach_sum(target, next_values)
    return possible_ways


def part1(numbers: tuple[int]):
    print(f'The number of ways to transfer 150 gallons is {count_possible_ways_to_reach_sum(150, numbers)}')


def main():
    with open('input17.txt') as f:
        numbers = list(map(int, f.readlines()))
        numbers.sort(reverse=True)
        part1(tuple(numbers))


if __name__ == '__main__':
    main()
