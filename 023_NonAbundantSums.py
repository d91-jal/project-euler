__author__ = 'johan'



# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
# 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
# if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as
# the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
# than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced
# any further by analysis even though it is known that the greatest number that cannot be expressed as the
# sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from ProjectEuler.divisors import iter_divisors

abu = []

for number, divisors in enumerate(iter_divisors(28123)):
    divs = divisors[:-1]

    if sum(divs) > number:
        abu.append([number, divs])

# Extract the abundant numbers.
a = [n[0] for n in abu]
print(len(a), a)

abusums = {}

for i in range(len(a)):
    for j in range(i, len(a)):
        temp = a[i] + a[j]

        if temp > 28123:
            break
        else:
            abusums[temp] = temp

sum = 28123 * (28124 / 2)

for i in abusums.keys():
    sum -= i

print(sum)


print(abusums)







