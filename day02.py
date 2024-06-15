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


def part1():
    with open("input02.txt") as f:
        needed_wrapping_paper = 0
        for line in f.readlines():
            needed_wrapping_paper += calculate_needed_wrapping_paper(parse_box_dimensions(line.strip()))
        print(f"Day 2, part 1: Needed wrapping paper {needed_wrapping_paper}")


def main():
    part1()


if __name__ == "__main__":
    main()
