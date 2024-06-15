from hashlib import md5


def find_smallest_number_with_five_leading_zeroes(secret: str) -> int:
    value = 0
    while True:
        test_source = secret + str(value)
        hash_output = md5(test_source.encode())
        hash_string = hash_output.hexdigest()
        if hash_string.startswith('00000'):
            return value
        value += 1


def part1():
    number = find_smallest_number_with_five_leading_zeroes('iwrupvqb')
    print(f'Day 4, part 1: The smallest number that has a hash starting with 5 zeroes is {number}')



def main():
    part1()


if __name__ == '__main__':
    main()