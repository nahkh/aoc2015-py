from __future__ import annotations
import dataclasses
from typing import List, Generator, Iterable, Tuple


@dataclasses.dataclass(frozen=True)
class Replacement:
    source: str
    result: str

    @classmethod
    def parse(cls, line: str) -> Replacement:
        parts = line.strip().split(' => ')
        assert len(parts) == 2, f'Unexpected split of "{line}"'
        name = parts[0]
        result = parts[1]
        return Replacement(name, result)

    def apply(self, molecule: str) -> Generator[str]:
        index = 0
        while index >= 0:
            if self.source not in molecule[index:]:
                return
            index = molecule.index(self.source, index)
            if index >= 0:
                yield molecule[0:index] + self.result + molecule[index + len(self.source):]
                index += 1


@dataclasses.dataclass(frozen=True)
class MedicinePlant:
    medicine_molecule: str
    replacements: Tuple[Replacement]


    @classmethod
    def parse(cls, lines: List[str]) -> MedicinePlant:
        processing_replacements = True
        replacements = []
        medicine_molecule = None
        for line in lines:
            line = line.strip()
            if not line:
                assert processing_replacements, 'Two empty lines encountered, panic'
                processing_replacements = False
                continue
            if processing_replacements:
                replacements.append(Replacement.parse(line))
            else:
                assert not medicine_molecule, 'A second medicine molecule encountered, panic'
                medicine_molecule = line
        assert replacements, 'We should have found at least one replacement'
        assert not processing_replacements, 'We should have stopped processing replacements'
        assert medicine_molecule, 'We did not encounter a medicine molecule'
        return MedicinePlant(medicine_molecule, tuple(replacements))

    def count_distinct_replacements(self) -> int:
        molecules = set()
        for replacement in self.replacements:
            for molecule in replacement.apply(self.medicine_molecule):
                molecules.add(molecule)
        return len(molecules)


def part1(plant: MedicinePlant):
    print(f'Day 19, part 1: The number of distinct molecules is {plant.count_distinct_replacements()}')


def main():
    with open('input19.txt') as f:
        plant = MedicinePlant.parse(f.readlines())
        part1(plant)


if __name__ == '__main__':
    main()
