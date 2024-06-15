from __future__ import annotations
import dataclasses
from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    @classmethod
    def parse(cls, character: str) -> Direction:
        if character == 'v':
            return Direction.SOUTH
        elif character == '^':
            return Direction.NORTH
        elif character == '>':
            return Direction.EAST
        elif character == '<':
            return Direction.WEST
        else:
            assert False, f'Unknown character "{character}"'

    def as_position(self) -> Position:
        if self == Direction.NORTH:
            return Position(0, 1)
        elif self == Direction.SOUTH:
            return Position(0, -1)
        elif self == Direction.WEST:
            return Position(-1, 0)
        elif self == Direction.EAST:
            return Position(1, 0)
        else:
            assert False, f'Unhandled direction {self}'


@dataclasses.dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other: Position) -> Position:
        assert isinstance(other, Position), f'Invalid type for addition, {other} is of class {type(other)}'
        return Position(self.x + other.x, self.y + other.y)


def part1(instructions):
    position = Position(0, 0)
    visited_positions = {position}
    for character in instructions.strip():
        direction = Direction.parse(character)
        position += direction.as_position()
        visited_positions.add(position)
    print(f'Day 3, part 1: Santa visited {len(visited_positions)} houses at least once')


def part2(instructions):
    position_a = Position(0, 0)
    position_b = Position(0, 0)
    a_is_moving = True
    visited_positions = {position_a}
    for character in instructions.strip():
        direction = Direction.parse(character)
        if a_is_moving:
            position_a += direction.as_position()
            visited_positions.add(position_a)
        else:
            position_b += direction.as_position()
            visited_positions.add(position_b)
        a_is_moving = not a_is_moving

    print(f'Day 3, part 2: Santa and robot santa visited {len(visited_positions)} houses at least once')



def main():
    with open('input03.txt') as f:
        instructions = f.readline()
        part1(instructions)
        part2(instructions)


if __name__ == '__main__':
    main()