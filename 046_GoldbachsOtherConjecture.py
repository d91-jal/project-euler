
# It was proposed by Christian Goldbach that every odd composite number can be written as the
# sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#
# Approach: Generate all possible combinations of prime + 2 * square until we find a missing odd composite.

from ProjectEuler.primes import eratosthenes_sieve
import math

upper_bound = 10000
primes = [p for p in eratosthenes_sieve(upper_bound) if p > 2]


def generate_odd_composites():
    odd_composites = [odd for odd in range(9, primes[-1] + 2, 2) if odd not in primes]
    return odd_composites


def generate_goldbach():
    goldbach_composites = [(p + 2*i*i) for p in primes for i in range(1, int(math.sqrt(upper_bound)))
                           if (p + 2*i*i) < upper_bound and (p + 2*i*i) not in primes]
    return goldbach_composites


#print(primes)
#print(generate_goldbach())
odd_composites = generate_odd_composites()
goldbach = generate_goldbach()
non_goldbach_composites = [comp for comp in odd_composites if comp not in goldbach]
print(non_goldbach_composites)
