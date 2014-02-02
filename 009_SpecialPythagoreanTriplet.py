__author__ = 'johan'



# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Reduce the equations a bit...
# c = 1000 - (a + b)
# c = math.sqrt(a^2 + b^2)
# a^2 + b^2 = 1e6 + a^2 + b^2 + 2ab - 2000(a + b)
# 2ab - 2000a - 2000b + 1e6 = 0
# 2a(b - 1000) = 2000b - 1e6
# a = (1000b - 5e5) / (b - 1000)

for a in range(1, 500):
    b = (1000 * a - 500000) / (a - 1000)
    c = 1000 - (a + b)

    if(a % 1 == 0 and b % 1 == 0):
        print(a, b, c, a + b + c, a * b * c)

    if a >= b: break



