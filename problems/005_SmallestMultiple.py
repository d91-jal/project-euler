__author__ = 'johan'

# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

from operator import mul
from functools import reduce


def find_primes(lower, upper):
    if upper < 2 or upper < lower:
        return []

    primes = [2, 3]

    # Loop over all odd integers from 3 to the upper bound.
    for i in range(5, upper + 1, 2):
        # If the number is indivisible by any lower number
        # then it is a candidate...
        candidate = True

        for j in range(3, i + 1, 2):
            # print(i, j, i%j)
            if i % j == 0:
                break

            for p in primes:
                # ...unless it is also divisible by a factor we have found already.
                if i % p == 0:
                    candidate = False
                    break

            if candidate:
                primes.append(i)

    return primes


# print(find_primes(0, 200))


def find_lowest_evenly_divisible_by_all_numbers_in_range(lower, upper):
    result = []
    primes = find_primes(0, upper)

    # Find the largest prime factor fitting in the range (i.e. if the range
    # is 1-10 the largest factor of 2 is 8, of 3 is 9...
    for i in primes:
        if i > upper:
            break
        else:
            x = 2

            while i ** x < upper + 1:
                x += 1

            result.append(i ** (x - 1))

    return result


a = find_lowest_evenly_divisible_by_all_numbers_in_range(1, 20)
print(a)

# Note: reduce removed from basic Python in ver 3.x
b = reduce(mul, a)

print(b)




