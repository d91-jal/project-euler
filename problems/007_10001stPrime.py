__author__ = 'johan'

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?


from ProjectEuler.utils.primes import eratosthenes_sieve

a = [p for p in eratosthenes_sieve(11000000)]
print(len(a), a[-1])

if len(a) > 500000:
    print('10001st prime:', a[10000])
    print('prime 5\t\t\t:', a[4])
    print('prime 50\t\t:', a[49])
    print('prime 500\t\t:', a[499])
    print('prime 5000\t\t:', a[4999])
    print('prime 50000\t\t:', a[49999])
    print('prime 500000\t:', a[499999])
