# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from ProjectEuler.utils.primes import eratosthenes_sieve


def find_prime_as_sum_of_consecutive_primes(ceiling):
    primes = [p for p in eratosthenes_sieve(ceiling)]
    max_length = 0

    for i in range(0, len(primes)):
        for j in range(i+1, len(primes)):
            next_sum = sum(primes[i:j])

            if next_sum > ceiling:
                break

            if next_sum in primes:
                if j - i > max_length:
                    max_length = j - i
                    total = next_sum
                    print(total, j-i)


find_prime_as_sum_of_consecutive_primes(999999)
