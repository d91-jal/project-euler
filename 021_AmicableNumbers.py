__author__ = 'johan'

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ? b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
import math

def FindDivisorSum(top):
    result = [0]

    for i in range(1, top + 1):
        temp = []

        # Find all divisors up to the square root.
        for j in range(1, math.ceil(math.sqrt(i)) + 1):
            if i % j == 0:
                temp.append(j)

        # Calculate all divisors larger than the square root.
        temp.extend([int(i / k) for k in temp if k > 1])

        #if i == 220: print(temp)
        result.append(sum(temp))

    return result

def FindAmicable(divsums):
    result = []

    for i in range(2, len(divsums)):
        a = divsums[i]

        if a < len(divsums):
            b = divsums[a]
            #print(i, a, b)

            if b == i and b != a:
                result.append(a)

    return result

a = 10000
b = FindDivisorSum(a)

#for i in range(len(b)):
#    if b[i] < len(b):
#        print(i, b[i], b[b[i]])

amicable = FindAmicable(b)

#print(b)
print(sum(amicable), amicable)

