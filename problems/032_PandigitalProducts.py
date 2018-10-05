__author__ = 'johan'

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and
# product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through
# 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# Generate all products x * y = z resulting in a total of 9 digits for x, y and z.
# 1 * 9999 = 9999
# 10 * 999 = 9990
# 99 * 101 = 9999


def is_pan_digital(a, b, c):
    chars = str(a) + str(b) + str(c)
    result = ''.join(sorted(chars))
    return result == '123456789'


# print(is_pan_digital(1, 2, 3))
# print(is_pan_digital(345, 345, 345))
# print(is_pan_digital(123, 456, 789))
# print(is_pan_digital(7, 31, 245689))
# print(is_pan_digital(39, 186, 7254))

result = []

for x in range(1, 99):
    y = 1000 // x
    product = 0

    while product < 9876:
        product = x * y

        if is_pan_digital(x, y, product):
            result.append([x, y, product])

        y += 1

unique = set([i[-1] for i in result])

print(result)
print(sum(unique), unique)


