from __future__ import annotations
import dataclasses
from typing import List, Generator


@dataclasses.dataclass(frozen=True)
class Position:
    x: int
    y: int

    def neighbors(self) -> Generator[Position]:
        yield Position(self.x - 1, self.y - 1)
        yield Position(self.x - 1, self.y)
        yield Position(self.x - 1, self.y + 1)
        yield Position(self.x, self.y - 1)
        yield Position(self.x, self.y + 1)
        yield Position(self.x + 1, self.y - 1)
        yield Position(self.x + 1, self.y)
        yield Position(self.x + 1, self.y + 1)


@dataclasses.dataclass(frozen=True)
class GridState:
    step: int = dataclasses.field(compare=False)
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    enabled_lights: frozenset[Position]

    @classmethod
    def parse(cls, lines: List[str]) -> GridState:
        enabled_lights = set()
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                if c == '#':
                    enabled_lights.add(Position(x, y))
        min_x = min(map(lambda z: z.x, enabled_lights))
        max_x = max(map(lambda z: z.x, enabled_lights))
        min_y = min(map(lambda z: z.y, enabled_lights))
        max_y = max(map(lambda z: z.y, enabled_lights))
        return GridState(0, min_x, max_x, min_y, max_y, frozenset(enabled_lights))

    def count_lit_neighbors(self, position: Position) -> int:
        lit_neighbors = 0
        for neighbor in position.neighbors():
            if neighbor in self.enabled_lights:
                lit_neighbors += 1
        return lit_neighbors

    def is_new_state_lit(self, position: Position) -> bool:
        lit_neighbors = self.count_lit_neighbors(position)
        if position in self.enabled_lights:
            return 2 <= lit_neighbors <= 3
        else:
            return lit_neighbors == 3

    def positions(self) -> Generator[Position]:
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                yield Position(x, y)

    def iterate(self) -> GridState:
        new_lights = set()
        for position in self.positions():
            if self.is_new_state_lit(position):
                new_lights.add(position)
        return GridState(self.step + 1, self.min_x, self.max_x, self.min_y, self.max_y, frozenset(new_lights))

    def count_lit_lights(self) -> int:
        return len(self.enabled_lights)


def part1(initial_state: GridState):
    number_of_steps = 100
    state = initial_state
    for i in range(number_of_steps):
        state = state.iterate()
    print(f'Day 18, part 1: The number of lit lights after {number_of_steps} steps is {state.count_lit_lights()}')


def main():
    with open('input18.txt') as f:
        initial_state = GridState.parse(f.readlines())
        part1(initial_state)


if __name__ == '__main__':
    main()
