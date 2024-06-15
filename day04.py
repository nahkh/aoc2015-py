from hashlib import md5


def find_smallest_number_with_n_leading_zeroes(n: int, secret: str) -> int:
    prefix = '0' * n
    value = 0
    while True:
        test_source = secret + str(value)
        hash_output = md5(test_source.encode())
        hash_string = hash_output.hexdigest()
        if hash_string.startswith(prefix):
            return value
        value += 1


def part1():
    number = find_smallest_number_with_n_leading_zeroes(5, 'iwrupvqb')
    print(f'Day 4, part 1: The smallest number that has a hash starting with 5 zeroes is {number}')


def part2():
    number = find_smallest_number_with_n_leading_zeroes(6, 'iwrupvqb')
    print(f'Day 4, part 2: The smallest number that has a hash starting with 6 zeroes is {number}')


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()