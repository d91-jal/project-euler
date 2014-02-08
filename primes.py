__author__ = 'johan'

import math

primes_db_file = r'primes.txt'


def eratosthenes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i

            for n in range(i * i, limit, i):     # Mark factors non-prime
                a[n] = False

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




