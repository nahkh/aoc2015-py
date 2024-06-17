from __future__ import annotations
from typing import List, Tuple
import dataclasses

HEX_CHARS = frozenset('0123456789abcdef')


@dataclasses.dataclass(frozen=True)
class LineConsumer:
    in_memory_characters: int
    in_storage_characters: int
    tail: str

    @classmethod
    def create(cls, content: str) -> LineConsumer:
        content = content.strip()
        assert len(content) >= 2 and content[0] == '"' and content[-1] == '"', f'Line "{content}" does not start and end with quotes'
        return LineConsumer(0, 2, content[1:-1])

    def is_finished(self) -> bool:
        return not self.tail

    # Note that this class could have been implemented as a mutable class; that would also work in this case. However,
    # immutable data has many benefits, so I try to use it whenever possible.
    def process(self) -> LineConsumer:
        if self.is_finished():
            return self
        if self.tail.startswith('\\\\'):
            return LineConsumer(self.in_memory_characters + 1, self.in_storage_characters + 2, self.tail[2:])
        elif self.tail.startswith('\\"'):
            return LineConsumer(self.in_memory_characters + 1, self.in_storage_characters + 2, self.tail[2:])
        elif self.tail.startswith('\\x'):
            if len(self.tail) >= 4 and self.tail[2] in HEX_CHARS and self.tail[3] in HEX_CHARS:
                return LineConsumer(self.in_memory_characters + 1, self.in_storage_characters + 4, self.tail[4:])
        return LineConsumer(self.in_memory_characters + 1, self.in_storage_characters + 1, self.tail[1:])


def count_characters(line: str) -> Tuple[int, int]:
    line_consumer = LineConsumer.create(line)
    while not line_consumer.is_finished():
        line_consumer = line_consumer.process()
    return line_consumer.in_storage_characters, line_consumer.in_memory_characters


def summary_difference(lines: List[str]) -> Tuple[int, int, int]:
    in_storage = 0
    in_memory = 0
    for line in lines:
        a, b = count_characters(line)
        in_storage += a
        in_memory += b
    return in_storage, in_memory, in_storage - in_memory


def part1(lines: List[str]):
    in_storage, in_memory, diff = summary_difference(lines)
    print('Day 8, part 1:')
    print(f'  The number of characters in storage {in_storage}')
    print(f'  The number of characters in memory {in_memory}')
    print(f'  The difference: {diff}')


def encode(line: str) -> str:
    output = '"'
    for c in line:
        if c == '"':
            output += '\\"'
        elif c == '\\':
            output += '\\\\'
        else:
            output += c
    return output + '"'


def part2(lines: List[str]):
    in_storage, in_memory, diff = summary_difference(list(map(encode, lines)))
    print('Day 8, part 2:')
    print(f'  The number of characters in storage {in_storage}')
    print(f'  The number of characters in memory {in_memory}')
    print(f'  The difference: {diff}')


def main():
    with open('input08.txt') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


if __name__ == '__main__':
    main()
