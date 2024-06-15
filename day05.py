from __future__ import annotations
from typing import List


VOWELS = frozenset('aeiou')
BAD_SUBSTRINGS = 'ab', 'cd', 'pq', 'xy'


def count_vowels(line: str) -> int:
    return sum(map(lambda x: 1 if x in VOWELS else 0, line))


def has_three_vowels(line: str) -> bool:
    return count_vowels(line) >= 3


def contains_two_consecutive_characters(line: str) -> bool:
    # If the line is empty, return early
    if not line:
        return False
    previous = line[0]
    for i in range(1, len(line)):
        next_char = line[i]
        if next_char == previous:
            return True
        previous = next_char
    return False


def does_not_contain_bad_substrings(line: str) -> bool:
    for bad_substring in BAD_SUBSTRINGS:
        if bad_substring in line:
            return False
    return True


def is_nice(line: str) -> bool:
    return has_three_vowels(line) and contains_two_consecutive_characters(line) and does_not_contain_bad_substrings(line)


def part1(lines: List[str]):
    nice_line_count = 0
    for line in lines:
        if is_nice(line):
            nice_line_count += 1
    print(f'Day 5, part 1: The list has {nice_line_count} nice lines')


def generate_all_characters():
    for index in range(ord('a'), ord('z') + 1):
        yield chr(index)


def generate_all_pairs():
    for first in generate_all_characters():
        for second in generate_all_characters():
            yield first + second


def line_contains_two_pairs(line: str, pair: str) -> bool:
    try:
        first_index = line.index(pair)
        line.index(pair, first_index + 2)
        return True
    except ValueError:
        return False


def line_contains_any_two_pairs(line: str) -> bool:
    for pair in generate_all_pairs():
        if line_contains_two_pairs(line, pair):
            return True
    return False


def contains_two_consecutive_characters_separated_by_one(line: str) -> bool:
    # If the line is too short, return early
    if len(line) < 3:
        return False
    previous = line[0]
    middle = line[1]
    for i in range(2, len(line)):
        next_char = line[i]
        if next_char == previous:
            return True
        previous = middle
        middle = next_char
    return False


def is_really_nice(line: str) -> bool:
    return contains_two_consecutive_characters_separated_by_one(line) and line_contains_any_two_pairs(line)


def part2(lines: List[str]):
    nice_line_count = 0
    for line in lines:
        if is_really_nice(line):
            nice_line_count += 1
    print(f'Day 5, part 2: The list has {nice_line_count} nice lines')


def main():
    with open('input05.txt') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


if __name__ == '__main__':
    main()
