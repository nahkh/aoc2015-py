from __future__ import annotations
import dataclasses
from functools import cache
from typing import Dict, List
from collections import defaultdict


@dataclasses.dataclass(frozen=True)
class Property:
    is_known: bool
    value: int

    @classmethod
    @cache
    def unknown(cls) -> Property:
        return Property(False, 0)

    @classmethod
    def known(cls, value: int) -> Property:
        return Property(True, value)

    def is_possible(self, measurement: int) -> bool:
        return not self.is_known or self.value == measurement


@dataclasses.dataclass
class AuntSue:
    identifier: int
    known_properties: Dict[str, Property]

    @classmethod
    def parse(cls, line: str) -> AuntSue:
        identifier_index = line.index(':')
        identifier = int(line[4:identifier_index])
        properties = line[identifier_index + 2:].split(', ')
        known_properties = defaultdict(Property.unknown)
        for property_description in properties:
            split_property = property_description.split(': ')
            name = split_property[0]
            assert name == name.strip()
            amount = int(split_property[1])
            known_properties[name] = Property.known(amount)
        return AuntSue(identifier, known_properties)

    def is_possible(self, measurements: Dict[str, int]) -> bool:
        for property_name, measurement in measurements.items():
            if not self.known_properties[property_name].is_possible(measurement):
                return False
        return True


def part1(aunts: List[AuntSue]):
    measurements = {'children': 3,
                    'cats': 7,
                    'samoyeds': 2,
                    'pomeranians': 3,
                    'akitas': 0,
                    'vizslas': 0,
                    'goldfish': 5,
                    'trees': 3,
                    'cars': 2,
                    'perfumes': 1}
    for aunt in aunts:
        if aunt.is_possible(measurements):
            print(f'Aunt {aunt.identifier} is possible')


def main():
    with open('input16.txt') as f:
        aunts = [AuntSue.parse(line) for line in f.readlines()]
        part1(aunts)


if __name__ == '__main__':
    main()
