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
    max_length = 1
    total = 0

    for i in range(0, len(primes)):
        # If no better solution is possible, we're done.
        if i > (len(primes) - max_length):
            break

        for j in range(i + max_length, len(primes)):
            next_sum = sum(primes[i:j+1])

            if next_sum > ceiling:
                break

            if next_sum in primes:
                if j - i > max_length:
                    max_length = j - i
                    total = next_sum
                    # print(total, i, j, new_prime)

    return total


print(find_prime_as_sum_of_consecutive_primes(999))
print(find_prime_as_sum_of_consecutive_primes(9999))
print(find_prime_as_sum_of_consecutive_primes(99999))
print(find_prime_as_sum_of_consecutive_primes(999999))
