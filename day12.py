from __future__ import annotations
from typing import Generator
import json

def parse_numbers(line: str) -> Generator[int]:
    currently_processing_number = False
    current_number = 0
    sign = 1
    for c in line:
        if not currently_processing_number:
            if c == '-':
                currently_processing_number = True
                current_number = 0
                sign = -1
            elif c.isdigit():
                currently_processing_number = True
                current_number = int(c)
                sign = 1
        else:
            if c.isdigit():
                current_number = current_number * 10 + int(c)
            else:
                yield sign * current_number
                sign = 1
                current_number = 0
                currently_processing_number = False
    if currently_processing_number:
        yield sign * current_number


def sum_numbers(line: str) -> int:
    return sum(parse_numbers(line))


def part1(line: str):
    print(f'Day 12, part 1: The sum numbers is {sum_numbers(line)}')


def prune_reds(obj):
    if isinstance(obj, dict):
        contains_red = False
        for key, value in obj.items():
            if value == 'red':
                contains_red = True
                break
        if contains_red:
            return {}
        else:
            return {key: prune_reds(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [prune_reds(item) for item in obj]
    else:
        return obj


def sum_numbers_without_reds(line: str) -> int:
    obj = json.loads(line)
    obj = prune_reds(obj)
    new_line = json.dumps(obj)
    return sum(parse_numbers(new_line))


def part2(line: str):
    print(f'Day 12, part 2: The sum numbers without reds is {sum_numbers_without_reds(line)}')


def main():
    with open('input12.txt') as f:
        line = f.readline()
        part1(line)
        part2(line)


if __name__ == '__main__':
    main()
