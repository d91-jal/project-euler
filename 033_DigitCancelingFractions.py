__author__ = 'johan'

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
# it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and
# containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import gcd

result = []

def part(x, idx):
    return int(str(x)[-idx])


for i in range(10, 99):
    for j in range(i + 1, 100):
        i1 = part(i, 1)
        i10 = part(i, 2)
        j1 = part(j, 1)
        j10 = part(j, 2)

        if j1 != 0 and i1 != i10 and i1 == j10 and i / j == i10 / j1:
            result.append([i, j]) # Use the smaller fraction since we aim to reduce the product afterwards.

print(result)

products = [1, 1]

for i in result:
    products[0] *= i[0]
    products[1] *= i[1]

divisor = gcd(products[0], products[1])

print(products, [i // divisor for i in products])
