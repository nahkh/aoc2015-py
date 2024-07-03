from __future__ import annotations
from typing import Generator, Tuple, Dict
import dataclasses
import math
from functools import reduce


@dataclasses.dataclass
class PrimeCache:
    primes: tuple[int]

    @classmethod
    def create(cls, max_prime: int):
        sieve = [True] * (max_prime + 2)
        for i in range(2, math.ceil(math.sqrt(max_prime)) + 1):
            j = 2
            while i * j < len(sieve):
                sieve[i*j] = False
                j += 1
        primes = []
        for i in range(2, len(sieve)):
            if sieve[i]:
                primes.append(i)
        return PrimeCache(tuple(primes))

    def factorize(self, n: int) -> Dict[int, int]:
        results = {}
        for prime in self.primes:
            while n % prime == 0:
                results[prime] = results.get(prime, 0) + 1
                n = n // prime
            if n == 1:
                return results
        assert False, f'We should not have reached here: {n} remains'

    def get_divisors(self, n: int) -> Generator[int]:
        if n == 1:
            yield 1
            return
        factors = [x for x in self.factorize(n).items()]
        nfactors = len(factors)
        f = [0] * nfactors
        while True:
            yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
            i = 0
            while True:
                f[i] += 1
                if f[i] <= factors[i][1]:
                    break
                f[i] = 0
                i += 1
                if i >= nfactors:
                    return

    def sum_of_divisors(self, n: int) -> int:
        result = 1
        for prime, m in self.factorize(n).items():
            result *= (prime ** (m+1) - 1) // (prime - 1)
        return result


def get_number_of_presents(prime_cache: PrimeCache, house_number: int) -> int:
    return 10 * prime_cache.sum_of_divisors(house_number)


def part1(min_presents: int):
    primes = PrimeCache.create(min_presents // 10)
    best_presents = 0
    current_house = 0
    while best_presents < min_presents:
        current_house += 1
        presents = get_number_of_presents(primes, current_house)
        if presents > best_presents:
            best_presents = presents

    print(f'Day 20, part 1: House {current_house} got {best_presents}')


def main():
    part1(33100000)


if __name__ == '__main__':
    main()
