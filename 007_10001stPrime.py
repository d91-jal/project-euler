__author__ = 'johan'

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?


from ProjectEuler.primes import eratosthenes_sieve


a = [p for p in eratosthenes_sieve(110000)]
print(len(a), a[-1])

if len(a) > 10000: print('10001st prime:', a[10000])