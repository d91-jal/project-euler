__author__ = 'johan'

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from ProjectEuler.primes import eratosthenes_sieve

a = eratosthenes_sieve(2000000)
print(len(a), a[-1])

print(sum(a))