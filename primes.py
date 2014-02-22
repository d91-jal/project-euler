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


def find_prime_factors(number):
    upper = math.floor(math.sqrt(number))
    prime_factors = []

    # Loop over all integers from 2 to the truncated
    # square root of the supplied number.
    for i in range(2, upper + 1):
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

    return prime_factors


def eratosthenes_sieve_old(upper):
    remaining = [1, 2] + ([i for i in range(3, upper + 1, 2)])
    #print(remaining)
    stop_value = math.ceil(math.sqrt(upper + 1))
    #print(stop_value)
    index = 1
    latest = remaining[2]
    print('Verifying primes from 2 to {0} will filter out all primes from 2 to {1}'.format(stop_value, upper))

    while latest <= stop_value:
        #print(latest)
        # Scratch all multiples of latest
        for i in range(len(remaining) - 1, index + 1, -1):
            if(remaining[i] % latest == 0):
                remaining.pop(i)

        index += 1
        latest = remaining[index]

        if (index % 10) == 0:
            print('Verified {0} primes, last prime = {1}'.format(index, latest))

    return remaining

#a = eratosthenes_sieve(2000000)
#print(len(a), a[-1])

#if len(a) > 10000: print('10001st prime:', a[10000])




