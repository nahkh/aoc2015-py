from __future__ import annotations
import dataclasses
import itertools
from typing import Dict, List, Iterable


@dataclasses.dataclass
class Person:
    name: str
    preferences: Dict[str, int]

    def __add__(self, other: Person) -> int:
        assert isinstance(other, Person), f'{other} is not a Person'
        return self.preferences[other.name] + other.preferences[self.name]

@dataclasses.dataclass
class Table:
    people: List[Person]
    names: tuple[str, ...]
    name_to_person: Dict[str, Person]

    @classmethod
    def parse(cls, lines: List[str]) -> Table:
        people = []
        current_name = None
        current_preferences = {}
        for line in lines:
            line = line.replace('would ', '').replace('gain ', '').replace('lose ', '-').replace(
                'happiness units by sitting next to ', '').replace('.', '').strip()
            parts = line.split(' ')
            name = parts[0]
            happiness_change = int(parts[1])
            neighbor = parts[2]
            if name != current_name and current_name is not None:
                people.append(Person(current_name, current_preferences))
                current_preferences = {}
            current_name = name
            current_preferences[neighbor] = happiness_change
        if current_name is not None:
            people.append(Person(current_name, current_preferences))
        return Table(people, tuple(map(lambda x: x.name, people)), {x.name: x for x in people})

    def evaluate_ordering(self, ordering: Iterable[str]) -> int:
        first = None
        previous = None
        value = 0
        for current_name in ordering:
            person = self.name_to_person[current_name]
            if not first:
                first = person
            if previous:
                value += previous + person
            previous = person
        if first and previous:
            value += first + previous
        return value

    def find_max_ordering(self) -> tuple[tuple[str, ...], int]:
        best_happiness_change = 0
        best_matching = None
        for ordering in itertools.permutations(self.names):
            value = self.evaluate_ordering(ordering)
            if not best_matching or best_happiness_change < value:
                best_happiness_change = value
                best_matching = tuple(ordering)
        return best_matching, best_happiness_change


def part1(lines: List[str]):
    table = Table.parse(lines)
    ordering, value = table.find_max_ordering()
    print(f'Day 13, part 1: The highest happiness change is {value}, with the following ordering:')
    print(f' {", ".join(ordering)}')


def main():
    with open('input13.txt') as f:
        lines = f.readlines()
        part1(lines)


if __name__ == '__main__':
    main()
