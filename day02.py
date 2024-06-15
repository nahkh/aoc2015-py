from typing import Tuple


def parse_box_dimensions(line: str) -> Tuple[int, int, int]:
    parts = tuple(map(int, line.split("x")))
    assert len(parts) == 3
    return parts


def calculate_needed_wrapping_paper(dimensions: Tuple[int, int, int]) -> int:
    length, width, height = dimensions
    sizes = [length * width, width * height, length * height]
    sizes.sort()
    return sizes[0] + 2 * sum(sizes)


def calculate_needed_ribbon(dimensions: Tuple[int, int, int]) -> int:
    length, width, height = dimensions
    perimiters = [2 * (length + width), 2 * (length + height), 2 * (height + width)]
    perimiters.sort()
    return perimiters[0] + length * width * height


def part1():
    with open("input02.txt") as f:
        needed_wrapping_paper = 0
        for line in f.readlines():
            needed_wrapping_paper += calculate_needed_wrapping_paper(parse_box_dimensions(line.strip()))
        print(f"Day 2, part 1: Needed wrapping paper {needed_wrapping_paper}")


def part2():
    with open("input02.txt") as f:
        needed_ribbon = 0
        for line in f.readlines():
            needed_ribbon += calculate_needed_ribbon(parse_box_dimensions(line.strip()))
        print(f"Day 2, part 2: Needed ribbon {needed_ribbon}")


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
