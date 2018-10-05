__author__ = 'johan'

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# 9! = 362880 => 7*9! = 2540160, 8*9! = 2903040 => 2540160 is an upper bound.

from math import factorial


def factorials(upper):
    result = []

    for i in range(upper + 1):
        result.append(factorial(i))

    return result


def digit_factorial_sum(i):
    temp = i
    num_sum = 0
    facts = factorials(9)

    while temp >= 1:
        num_sum += facts[temp % 10]
        # print(i, temp % 10, num_sum)
        temp //= 10

    return num_sum


facs = factorials(9)
combos = {}

for n in range(10, 7 * facs[9]):
    fact_sum = digit_factorial_sum(n)

    if fact_sum == n:
        combos[fact_sum] = fact_sum


print(combos)


# for i in range(11, 10000000):
#    if digit_factorial_sum(i) == i:
#        print(i)






