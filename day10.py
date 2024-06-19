from __future__ import annotations

import dataclasses
from typing import Generator


@dataclasses.dataclass(frozen=True)
class CharacterRun:
    character: str
    length: int

    @classmethod
    def create(cls, character: str, length: int) -> CharacterRun:
        assert len(character) == 1
        assert length > 0
        return CharacterRun(character, length)

    def __repr__(self) -> str:
        return str(self.length) + self.character


def split_characters(line: str) -> Generator[CharacterRun]:
    current_char = line[0]
    run_length = 1
    for c in line[1:]:
        if c != current_char:
            yield CharacterRun.create(current_char, run_length)
            current_char = c
            run_length = 1
        else:
            run_length += 1
    if current_char:
        yield CharacterRun.create(current_char, run_length)


def iterate(line: str) -> str:
    output = ''
    for run in split_characters(line):
        output += repr(run)
    return output


def part1():
    data = '1113122113'
    for i in range(40):
        data = iterate(data)
    print(f'Day 10, part 1: The length of the string after 40 iterations is {len(data)}')


def part2():
    data = '1113122113'
    for i in range(50):
        data = iterate(data)
    print(f'Day 10, part 2: The length of the string after 50 iterations is {len(data)}')


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
