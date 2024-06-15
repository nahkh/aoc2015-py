def calculate_reached_floor(instructions):
    current_floor = 0
    for c in instructions:
        if c == "(":
            current_floor += 1
        elif c == ")":
            current_floor -= 1
    return current_floor


def calculate_first_basement_position(instructions):
    current_floor = 0
    for i, c in enumerate(instructions):
        if c == "(":
            current_floor += 1
        elif c == ")":
            current_floor -= 1
        if current_floor == -1:
            return i + 1


def part1(instructions):
    print(f"Part 1: Reached floor {calculate_reached_floor(instructions)}")


def part2(instructions):
    print(f"Part 2: First reached basement in position {calculate_first_basement_position(instructions)}")


def main():
    with open("input01.txt") as f:
        instructions = f.readline()
        part1(instructions)
        part2(instructions)


if __name__ == "__main__":
    main()
