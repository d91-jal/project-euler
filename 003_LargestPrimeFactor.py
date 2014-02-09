__author__ = 'johan'

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

import math

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

print(find_prime_factors(13195))
print(find_prime_factors(600851475143))
