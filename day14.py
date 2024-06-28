from __future__ import annotations
import dataclasses
import itertools
import re
from typing import List

REINDEER_PATTERN = re.compile(r'^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')


@dataclasses.dataclass(frozen=True)
class Reindeer:
    name: str
    max_speed: int
    travel_time: int
    rest_time: int

    @classmethod
    def parse(cls, line: str) -> Reindeer:
        m = REINDEER_PATTERN.match(line)
        assert m, f'{line} did not match the expected pattern'
        name = m.group(1)
        speed = int(m.group(2))
        travel_time = int(m.group(3))
        rest_time = int(m.group(4))
        return Reindeer(name, speed, travel_time, rest_time)

    def distance_traveled(self, seconds: int) -> int:
        distance = 0
        for speed, max_time in itertools.cycle([(self.max_speed, self.travel_time), (0, self.rest_time)]):
            if max_time < seconds:
                seconds -= max_time
                distance += max_time * speed
            else:
                distance += seconds * speed
                return distance

    def as_racing(self) -> RacingReindeer:
        return RacingReindeer(self, 0)


@dataclasses.dataclass
class RacingReindeer:
    reindeer: Reindeer
    score: int


def parse_reindeers(lines: List[str]) -> List[Reindeer]:
    return [Reindeer.parse(line) for line in lines]


def part1(lines: List[str]):
    contest_time = 2503
    best = None
    best_distance = 0
    for reindeer in parse_reindeers(lines):
        distance = reindeer.distance_traveled(contest_time)
        if not best or best_distance < distance:
            best = reindeer
            best_distance = distance
    print(f'Day 14, part 1: The fastest reindeer was {best.name} with a distance of {best_distance}')


def part2(lines: List[str]):
    contest_time = 2503
    racing_reindeers = [Reindeer.parse(line).as_racing() for line in lines]
    for time in range(1, contest_time + 1):
        best = None
        best_distance = 0
        for racer in racing_reindeers:
            distance = racer.reindeer.distance_traveled(time)
            if not best or best_distance < distance:
                best = racer
                best_distance = distance
        best.score += 1
    overall_best = None
    for racer in racing_reindeers:
        if not overall_best or overall_best.score < racer.score:
            overall_best = racer
    print(f'Day 14, part 2: The best reindeer was {overall_best.reindeer.name} with a score of {overall_best.score}')


def main():
    with open('input14.txt') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


if __name__ == '__main__':
    main()
