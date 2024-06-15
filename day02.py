from __future__ import annotations
import dataclasses


@dataclasses.dataclass(frozen=True)
class Package:
    length: int
    width: int
    height: int

    @classmethod
    def parse(cls, line) -> Package:
        parts = tuple(map(int, line.split("x")))
        assert len(parts) == 3
        return Package(parts[0], parts[1], parts[2])

    def needed_wrapping_paper(self) -> int:
        sizes = [self.length * self.width, self.width * self.height, self.length * self.height]
        sizes.sort()
        return sizes[0] + 2 * sum(sizes)

    def needed_ribbon(self) -> int:
        perimeters = [2 * (self.length + self.width), 2 * (self.length + self.height), 2 * (self.height + self.width)]
        perimeters.sort()
        return perimeters[0] + self.length * self.width * self.height


def part1():
    with open("input02.txt") as f:
        needed_wrapping_paper = 0
        for line in f.readlines():
            needed_wrapping_paper += Package.parse(line.strip()).needed_wrapping_paper()
        print(f"Day 2, part 1: Needed wrapping paper {needed_wrapping_paper}")


def part2():
    with open("input02.txt") as f:
        needed_ribbon = 0
        for line in f.readlines():
            needed_ribbon += Package.parse(line.strip()).needed_ribbon()
        print(f"Day 2, part 2: Needed ribbon {needed_ribbon}")


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
