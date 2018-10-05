__author__ = 'johan'

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
# with denominators 2 to 10 are given:
#
#    1/2	= 	0.5
#    1/3	= 	0.(3)
#    1/4	= 	0.25
#    1/5	= 	0.2
#    1/6	= 	0.1(6)
#    1/7	= 	0.(142857)
#    1/8	= 	0.125
#    1/9	= 	0.(1)
#    1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7
# has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


# For each divisor: do long division until the remainder is 0 or repeated (cycle)
#
# E.g. for n = 3
# 10 / 3 = 3 remainder 1
# 10 / 3 = 3 remainder 1 => cycle
#
# n = 4
# 10 / 4 = 2 remainder 2
# 20 / 4 = 5 remainder 0 => done
#
# n = 5
# 10 / 5 = 2 remainder 0 => done
#
# n = 6
# 10 / 6 = 1 remainder 4
# 40 / 6 = 6 remainder 4
# 40 / 6 = 6 remainder 4 => done

max_cycle = (0, 0)

for i in range(1000, 1, -1):
    if i < max_cycle[1]:
        break

    remainder = 1
    remainders = []

    while remainder != 0:
        dividend = remainder * 10
        remainder = dividend % i

        if remainder in remainders:
            break

        remainders.append(remainder)

    if len(remainders) > max_cycle[1]:
        max_cycle = (i, len(remainders))

print(max_cycle)
