from __future__ import annotations
import dataclasses
from functools import cache
from typing import Dict, List
from collections import defaultdict
from enum import Enum


class MeasurementType(Enum):
    EXACT = 1
    LESS_THAN = 2
    GREATER_THAN = 3


@dataclasses.dataclass(frozen=True)
class Measurement:
    measurement_type: MeasurementType
    value: int

    @classmethod
    def exact(cls, value):
        return Measurement(MeasurementType.EXACT, value)

    @classmethod
    def greater_than(cls, value):
        return Measurement(MeasurementType.GREATER_THAN, value)

    @classmethod
    def less_than(cls, value):
        return Measurement(MeasurementType.LESS_THAN, value)


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

    def is_possible(self, measurement: Measurement) -> bool:
        if not self.is_known:
            return True
        if measurement.measurement_type == MeasurementType.EXACT:
            return self.value == measurement.value
        elif measurement.measurement_type == MeasurementType.GREATER_THAN:
            return self.value > measurement.value
        elif measurement.measurement_type == MeasurementType.LESS_THAN:
            return self.value < measurement.value
        else:
            assert False, f'Unsupported measurement type {measurement.measurement_type}'


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

    def is_possible(self, measurements: Dict[str, Measurement]) -> bool:
        for property_name, measurement in measurements.items():
            if not self.known_properties[property_name].is_possible(measurement):
                return False
        return True


def part1(aunts: List[AuntSue]):
    measurements = {'children': Measurement.exact(3),
                    'cats': Measurement.exact(7),
                    'samoyeds': Measurement.exact(2),
                    'pomeranians': Measurement.exact(3),
                    'akitas': Measurement.exact(0),
                    'vizslas': Measurement.exact(0),
                    'goldfish': Measurement.exact(5),
                    'trees': Measurement.exact(3),
                    'cars': Measurement.exact(2),
                    'perfumes': Measurement.exact(1)}
    for aunt in aunts:
        if aunt.is_possible(measurements):
            print(f'Day 16, part 1: Aunt {aunt.identifier} is possible')


def part2(aunts: List[AuntSue]):
    measurements = {'children': Measurement.exact(3),
                    'cats': Measurement.greater_than(7),
                    'samoyeds': Measurement.exact(2),
                    'pomeranians': Measurement.less_than(3),
                    'akitas': Measurement.exact(0),
                    'vizslas': Measurement.exact(0),
                    'goldfish': Measurement.less_than(5),
                    'trees': Measurement.greater_than(3),
                    'cars': Measurement.exact(2),
                    'perfumes': Measurement.exact(1)}
    for aunt in aunts:
        if aunt.is_possible(measurements):
            print(f'Day 16, part 2: Aunt {aunt.identifier} is possible')


def main():
    with open('input16.txt') as f:
        aunts = [AuntSue.parse(line) for line in f.readlines()]
        part1(aunts)
        part2(aunts)


if __name__ == '__main__':
    main()
