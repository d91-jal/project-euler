__author__ = 'johan'

# Euler discovered the remarkable quadratic formula:
#
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when
# n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
# The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the
# consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
#    n^2 + an + b, where |a| < 1000 and |b| < 1000
#
#    where |n| is the modulus/absolute value of n
#    e.g. |11| = 11 and |-4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression that produces the
# maximum number of primes for consecutive values of n, starting with n = 0.

# n*n + a*n + b = p
# Observations:
# n = 0 => p = b => b must be a prime
# n = 1 => 1 + a + b = p => a + b = p - 1 => always even => a must be odd (and a prime?)
# n = 2 => 4 + 2a + b = p
# a = (p - b - n*n) / n for all n > 0
# p - b will always be an even number (prime - prime)
# n*n is always odd if n is odd, always even if n is even.
#
# Let p be all primes from 1 to 1000 000.
# Let b be all primes from 1 to 1000.
# Let a be all numbers from 0 to 1000.

from ProjectEuler.utils.primes import eratosthenes_sieve

primes = [p for p in eratosthenes_sieve(100000)]
ax = [x for x in range(-999, 1001, 2)]
bx = [-x for x in primes if x < 1000]
bx.extend([-x for x in bx])

print(len(bx), bx)

result = (0, 0, 0)

# ax = [1]
# bx = [41]
# print((1 in ax), (41 in bx))

for a in ax:
    for b in bx:
        n = 0

        while (n * n) + (n * a) + b in primes:
            n += 1

        if n > result[0]:
            result = (n, a, b)

print(result)
