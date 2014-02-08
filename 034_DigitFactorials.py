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
    numSum = 0
    facs = factorials(9)

    while temp >= 1:
        numSum += facs[temp % 10]
        #print(i, temp % 10, numSum)
        temp //= 10

    return numSum


facs = factorials(9)
combos = {}

for i in range(10, 7 * facs[9]):
    temp = digit_factorial_sum(i)

    if temp == i:
        combos[temp] = temp


print(combos)


#for i in range(11, 10000000):
#    if digit_factorial_sum(i) == i:
#        print(i)






