from __future__ import annotations
import dataclasses
from typing import List, Generator, Iterable, Tuple, Set, Dict

PRACTICALLY_INFINITE = 1_000_000


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
        return Replacement._apply(molecule, self.source, self.result)

    def reverse(self, molecule: str) -> Generator[str]:
        return Replacement._apply(molecule, self.result, self.source)

    @staticmethod
    def _apply(molecule: str, source: str, result: str) -> Generator[str]:
        index = 0
        while index >= 0:
            if source not in molecule[index:]:
                return
            index = molecule.index(source, index)
            if index >= 0:
                yield molecule[0:index] + result + molecule[index + len(source):]
                index += 1

def replacement_value_heuristic(replacement: Replacement) -> int:
    value = 0
    if 'Ar' in replacement.result:
        value += 100
    value += len(replacement.result)
    value -= len(replacement.source)
    if replacement.source in replacement.result:
        value += 20
    if 'e' == replacement.source:
        value -= 10
    if replacement.result == 'CaCa':
        value += 5
    return value


@dataclasses.dataclass
class ResultReporter:
    best_reported: int

    @classmethod
    def create(cls):
        return ResultReporter(PRACTICALLY_INFINITE)

    def report(self, new_value: int):
        if new_value < self.best_reported:
            self.best_reported = new_value
            print(f'New shortest set of replacements is {new_value}')


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
        replacements.sort(key=replacement_value_heuristic, reverse=True)
        return MedicinePlant(medicine_molecule, tuple(replacements))

    def count_distinct_replacements(self) -> int:
        molecules = self.get_valid_replacements(self.medicine_molecule)
        return len(molecules)

    def get_valid_replacements(self, molecule: str) -> Set[str]:
        molecules = set()
        for replacement in self.replacements:
            for new_molecule in replacement.apply(molecule):
                molecules.add(new_molecule)
        return molecules

    def get_valid_precursors(self, molecule: str) -> Generator[str]:
        for replacement in self.replacements:
            for new_molecule in replacement.reverse(molecule):
                yield new_molecule

    def search(self, molecule: str = 'e', replacement_count: int = 0, best_known: int = PRACTICALLY_INFINITE) -> int:
        # Note that this approach does not work for larger graphs
        if molecule == self.medicine_molecule:
            return min(replacement_count, best_known)
        if len(molecule) > len(self.medicine_molecule):
            return PRACTICALLY_INFINITE
        for replacement in self.get_valid_replacements(molecule):
            best_known = min(self.search(replacement, replacement_count + 1, best_known), best_known)
        return best_known

    def reverse_search(self, molecule: str, replacement_count: int = 0, best_known: int = PRACTICALLY_INFINITE, cache: Dict[str, int] = None, result_reporter: ResultReporter = None) -> int:
        if not result_reporter:
            result_reporter = ResultReporter.create()
        if not cache:
            cache = {}
        if molecule in cache:
            return cache[molecule]
        if molecule == 'e':
            cache['e'] = min(replacement_count, best_known)
            result_reporter.report(replacement_count)
            return replacement_count
        if 'e' in molecule:
            cache[molecule] = PRACTICALLY_INFINITE
            # We know that there can only be one e, at the very beginning
            return PRACTICALLY_INFINITE
        if replacement_count > best_known:
            cache[molecule] = min(cache.get(molecule, PRACTICALLY_INFINITE), replacement_count)
            return best_known
        for precursor in self.get_valid_precursors(molecule):
            best_known = min(self.reverse_search(precursor, replacement_count + 1, best_known, cache, result_reporter), best_known)

        return best_known


def part1(plant: MedicinePlant):
    print(f'Day 19, part 1: The number of distinct molecules is {plant.count_distinct_replacements()}')


def part2(plant: MedicinePlant):
    print(f'Day 19, part 2: Searching for the shortest list of replacements')
    minimum_needed_replacements = plant.reverse_search(plant.medicine_molecule)
    print(f'The steps needed to make the medicine is {minimum_needed_replacements}')


def main():
    with open('input19.txt') as f:
        plant = MedicinePlant.parse(f.readlines())
        part1(plant)
        part2(plant)


if __name__ == '__main__':
    main()
