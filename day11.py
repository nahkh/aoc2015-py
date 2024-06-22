from __future__ import annotations


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


def password_is_valid(password: str) -> bool:
    pass
