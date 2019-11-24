__author__ = 'johan'

# The number 3797 has an interesting property. Being prime itself, it is possible to
# continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."

# Observation: No even numbers may be present in the primes.
# Optimizations to be made?

from utils.primes import eratosthenes_sieve

def truncate_left(num):
    if num < 10:
        return num

    return int(str(num)[1:])


def truncate_right(num):
    return num // 10


prime_list = [i for i in eratosthenes_sieve(1000001)]
prime_set = set(prime_list)
result = []

for prime in prime_list:
    if prime < 11:
        continue

    is_prime = True
    temp = prime

    while temp >= 10:
        temp = truncate_left(temp)
        is_prime = is_prime and temp in prime_set

    if is_prime:
        temp = prime

        while temp >= 10:
            temp = truncate_right(temp)
            is_prime = is_prime and temp in prime_set

    if is_prime:
        result.append(prime)

    if len(result) == 11:
        break

print(sum(result), result)
