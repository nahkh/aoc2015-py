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
    print(
        f'Day 17, part 1: The number of ways to transfer 150 gallons is {count_possible_ways_to_reach_sum(150, numbers)}')


@cache
def find_minimum_number_of_containers(target: int, values: Tuple[int], used_containers: int) -> int:
    if target == 0:
        return used_containers
    if len(values) == 0:
        return 0
    next_values = tuple(list(values)[1:])
    candidates = []
    if values[0] == target:
        return used_containers + 1
    elif values[0] < target:
        candidates.append(find_minimum_number_of_containers(target - values[0], next_values, used_containers + 1))
    candidates.append(find_minimum_number_of_containers(target, next_values, used_containers))
    nonzero_candidates = [candidate for candidate in candidates if candidate > 0]
    if nonzero_candidates:
        return min(nonzero_candidates)
    else:
        return 0


@cache
def count_possible_ways_to_reach_sum_with_n_containers(target: int, values: Tuple[int],
                                                       containers_remaining: int) -> int:
    if containers_remaining == 0:
        if target == 0:
            return 1
        else:
            return 0
    if containers_remaining == 1:
        return sum(1 for value in values if value == target)
    if len(values) == 0:
        return 0
    possible_ways = 0
    next_values = tuple(list(values)[1:])
    if values[0] == target and containers_remaining == 1:
        possible_ways += 1
    elif values[0] < target and containers_remaining > 1:
        possible_ways += count_possible_ways_to_reach_sum_with_n_containers(target - values[0], next_values,
                                                                            containers_remaining - 1)
    possible_ways += count_possible_ways_to_reach_sum_with_n_containers(target, next_values, containers_remaining)
    return possible_ways


def part2(numbers: tuple[int]):
    minimum_number_of_containers = find_minimum_number_of_containers(150, numbers, 0)
    number_of_ways = count_possible_ways_to_reach_sum_with_n_containers(150, numbers, minimum_number_of_containers)
    print(
        f'Day 17, part 2: The number of ways to transfer 150 gallons while using {minimum_number_of_containers} containers is {number_of_ways}')


def main():
    with open('input17.txt') as f:
        numbers = list(map(int, f.readlines()))
        numbers.sort(reverse=True)
        part1(tuple(numbers))
        part2(tuple(numbers))


if __name__ == '__main__':
    main()
