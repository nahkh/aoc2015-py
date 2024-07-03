from __future__ import annotations
from typing import Tuple, Optional


def get_first_house_with_n_presents(presents: int, presents_per_visit: int, max_visits: int = None) -> Tuple[int, int]:
    def depth_limited_search(depth: int) -> Optional[Tuple[int, int]]:
        present_counts = [presents_per_visit] * (depth + 1)
        for elf in range(2, depth + 1):
            index = elf
            present_counts[index] += presents_per_visit * elf
            if present_counts[elf] >= presents:
                return elf, present_counts[elf]
            visits = 1
            index += elf
            while index < len(present_counts) and (not max_visits or visits < max_visits):
                present_counts[index] += presents_per_visit * elf
                index += elf
                visits += 1
        for house in range(1, len(present_counts)):
            if present_counts[house] >= presents:
                return house, present_counts[house]
        return None

    current_depth = 1000000
    result = None
    while not result:
        result = depth_limited_search(current_depth)
        current_depth *= 10
    return result


def part1(min_presents: int):
    house, presents = get_first_house_with_n_presents(min_presents, 10)
    print(f'Day 20, part 1: House {house} got {presents}')


def part2(min_presents: int):
    house, presents = get_first_house_with_n_presents(min_presents, 11, 50)
    print(f'Day 20, part 2: House {house} got {presents}')


def main():
    part1(33100000)
    part2(33100000)


if __name__ == '__main__':
    main()
