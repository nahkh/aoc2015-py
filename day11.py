from __future__ import annotations
from functools import cache


def next_candidate(password: str) -> str:
    if not password:
        return password
    last_char = password[-1]
    prefix = password[:-1]
    next_last_char = ord(last_char) + 1
    if next_last_char > ord('z'):
        next_last_char = ord('a')
        prefix = next_candidate(prefix)
    return prefix + chr(next_last_char)


@cache
def get_straights():
    output = []
    for start in range(ord('a'), ord('y')):
        output.append(chr(start) + chr(start + 1) + chr(start + 2))
    return tuple(output)


def password_contains_increasing_straight(password: str) -> bool:
    for straight in get_straights():
        if straight in password:
            return True
    return False


def password_contains_two_pairs(password: str) -> bool:
    pair_count = 0
    prev_char = None
    for c in password:
        if c == prev_char:
            pair_count += 1
            prev_char = None
            continue
        prev_char = c
    return pair_count >= 2


def password_does_not_contain_banned_characters(password: str) -> bool:
    return 'i' not in password and 'o' not in password and 'l' not in password


def password_is_valid(password: str) -> bool:
    return password_contains_increasing_straight(password) and password_does_not_contain_banned_characters(
        password) and password_contains_two_pairs(password)


def find_next_valid_password(password: str) -> str:
    candidate = next_candidate(password)
    while not password_is_valid(candidate):
        candidate = next_candidate(candidate)
    return candidate


def part1():
    print(f'Day 11, part 1: Santa\'s next password will be {find_next_valid_password("cqjxjnds")}')


def main():
    part1()


if __name__ == '__main__':
    main()
