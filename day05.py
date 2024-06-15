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


def main():
    with open('input05.txt') as f:
        lines = f.readlines()
        part1(lines)


if __name__ == '__main__':
    main()
