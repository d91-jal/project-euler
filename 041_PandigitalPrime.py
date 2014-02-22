__author__ = 'johan'

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

# 9 digits => 987654321

from ProjectEuler.primes import eratosthenes_sieve, is_prime
from ProjectEuler.utils import is_pan_digital_number
from math import sqrt
from itertools import permutations


def generate_combos(start, end):
    factor = 1
    num = 0

    for i in range(end, start - 1, -1):
        num += i * factor
        factor *= 10

    return [int(''.join(p)) for p in permutations(str(num))]


def find_largest_pan_digital_prime():
    primes = [x for x in eratosthenes_sieve(int(sqrt(1e9)))]

    # Generate all pandigital numbers.
    pan_digs = []

    for i in range(1, 10):
        pan_digs += generate_combos(1, i)

    for i in range(len(pan_digs)):
        temp = pan_digs[-i]

        if temp % 2 == 0 or temp % 5 == 0:
            continue

        if is_prime(temp, primes):
            return temp

    return 1


print(find_largest_pan_digital_prime())
