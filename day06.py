from __future__ import annotations
import dataclasses
from enum import Enum
from typing import Generator, Tuple, Dict, List


@dataclasses.dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other: Position) -> Position:
        assert isinstance(other, Position), f'Invalid type for addition, {other} is of class {type(other)}'
        return Position(self.x + other.x, self.y + other.y)


@dataclasses.dataclass(frozen=True)
class PositionRange:
    left: int
    right: int
    top: int
    bottom: int

    @classmethod
    def parse(cls, content: str) -> PositionRange:
        parts = content.strip().split(' through ')
        assert len(parts) == 2
        assert ',' in parts[0]
        assert ',' in parts[1]
        lp = parts[0].split(',')
        x1 = int(lp[0])
        y1 = int(lp[1])
        rp = parts[1].split(',')
        x2 = int(rp[0])
        y2 = int(rp[1])
        left = min(x1, x2)
        right = max(x1, x2)
        top = min(y1, y2)
        bottom = max(y1, y2)
        return PositionRange(left, right, top, bottom)

    def positions(self) -> Generator[Position]:
        for x in range(self.left, self.right + 1):
            for y in range(self.top, self.bottom + 1):
                yield Position(x, y)


class InstructionType(Enum):
    TURN_ON = 1
    TURN_OFF = 2
    TOGGLE = 3

    @classmethod
    def parse(cls, line: str) -> Tuple[InstructionType, str]:
        if line.startswith('turn on '):
            return InstructionType.TURN_ON, line[8:]
        elif line.startswith('turn off '):
            return InstructionType.TURN_OFF, line[9:]
        elif line.startswith('toggle '):
            return InstructionType.TOGGLE, line[7:]
        else:
            assert False, f'Unable to parse instruction in line "{line}"'


@dataclasses.dataclass(frozen=True)
class Instruction:
    instruction_type: InstructionType
    position_range: PositionRange

    @classmethod
    def parse(cls, line: str) -> Instruction:
        instruction_type, remainder = InstructionType.parse(line)
        return Instruction(instruction_type, PositionRange.parse(remainder))


class LightState(Enum):
    ON = 1
    OFF = 2

    def apply(self, instruction: InstructionType) -> LightState:
        if instruction == InstructionType.TURN_ON:
            return LightState.ON
        elif instruction == InstructionType.TURN_OFF:
            return LightState.OFF
        elif instruction == InstructionType.TOGGLE:
            if self == LightState.ON:
                return LightState.OFF
            else:
                return LightState.ON
        else:
            assert False, f'Unhandled instruction {instruction}'


@dataclasses.dataclass
class LightField:
    field: Dict[Position, LightState]

    @classmethod
    def create(cls, width: int, height: int) -> LightField:
        return LightField({pos: LightState.OFF for pos in PositionRange(0, width - 1, 0, height - 1).positions()})

    def apply(self, instruction: Instruction):
        for position in instruction.position_range.positions():
            assert position in self.field, f'{position} out of bounds, in instruction {instruction}'
            self.field[position] = self.field[position].apply(instruction.instruction_type)

    def count_lights(self) -> int:
        total = 0
        for pos, light_state in self.field.items():
            if light_state == LightState.ON:
                total += 1
        return total


def part1(lines: List[str]):
    field = LightField.create(1000, 1000)
    for i, line in enumerate(lines):
        instruction = Instruction.parse(line)
        field.apply(instruction)
        print(f'{100 * i / len(lines):.2f}% complete')
    print(f'Day 6, part 1: The number of enabled lights is {field.count_lights()}')


def main():
    with open('input06.txt') as f:
        lines = f.readlines()
        part1(lines)


if __name__ == '__main__':
    main()