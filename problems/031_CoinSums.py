__author__ = 'johan'

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?

# Start with larger coins and work down.
#
# How many ways if we start with a £2 coin: 1
# How many ways if we start with a £1 coin: 1 + the number of ways to represent £1 with smaller coins.
# How many ways to represent £1 if we start with 50p : 1 + the number of ways to represent 50p with smaller coins.
# How many ways to represent 50p if we start with 20p : 1 + the number of ways to represent 30p with smaller coins.
# How many ways to represent 30p if we start with 20p : 1 + the number of ways to represent 10p with smaller coins.
# How many ways to represent 10p if we start with 5p : 1 + the number of ways to represent 5p with smaller coins =

# Number of ways to represent 0p : 1
# Number of ways to represent 1p : 1 (1)
# Number of ways to represent 2p : 2 (1+1, 2)
# Number of ways to represent 3p : 2 (1+1+1, 2+1)
# Number of ways to represent 4p : 3 (1+1+1+1, 2+1+1, 2+2)
# Number of ways to represent 5p : 4 (1+1+1+1+1, 2+1+1+1, 2+2+1, 5)
# ...

amount = 200
coinTypes = [1, 2, 5, 10, 20, 50, 100, 200]
combos = [0 for i in range(amount + 1)]
combos[0] = 1

for coin in coinTypes:
    for i in range(coin, amount + 1):
        combos[i] += combos[i - coin]

print(len(combos), combos)
