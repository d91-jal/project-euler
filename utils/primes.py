__author__ = 'johan'

import math

primes_db_file = r'primes.txt'


def eratosthenes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i

            for n in range(i * i, limit, i):     # Mark factors non-prime
                a[n] = False


def is_prime(num, primes):
    if num > max(primes) ** 2:
        AttributeError("num is too large to fit in the primes list.")

    if num in primes:
        return True

    if num < max(primes):
        return False

    for p in primes:
        if num % p == 0:
            return False

    return True


def find_prime_factors(number, primes):
    upper = math.ceil(math.sqrt(number) * 2)
    prime_factors = []

    # Loop over all integers from 2 to the truncated
    # square root of the supplied number.
    for i in primes:
        if i > upper:
            break

        # If the number is divisible by the current i
        # then it is a candidate...
        if number % i == 0:
            new_factor = True

            for p in prime_factors:
                # ...unless it is also divisible by a factor we have found already.
                if i % p == 0:
                    new_factor = False
                    break

            if new_factor:
                prime_factors.append(i)

    if len(prime_factors) == 0:
        prime_factors.append(number)

    return prime_factors


# a = eratosthenes_sieve(2000000)
# print(len(a), a[-1])

# if len(a) > 10000: print('10001st prime:', a[10000])




