# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19
#
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?
#
# Simple approach: Find the prime factors of any integer and find matching candidates.

from ProjectEuler.primes import find_prime_factors, eratosthenes_sieve
import math


def find_consecutive_integers_with_same_number_of_prime_factors(count):
    consecutive_found = 0
    limit = 300000
    primes = [p for p in eratosthenes_sieve(math.ceil(limit / 2))]

    for i in range(3, limit):
        factors = find_prime_factors(i, primes)
        # print(i, factors)

        if len(factors) == count:
            consecutive_found += 1

            if consecutive_found == count:
                return i-count+1
        else:
            consecutive_found = 0

    return 0


# print(find_consecutive_integers_with_same_number_of_prime_factors(2))
# print(find_consecutive_integers_with_same_number_of_prime_factors(3))
print(find_consecutive_integers_with_same_number_of_prime_factors(4))







