# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

from ProjectEuler.utils.primes import eratosthenes_sieve


def evaluate_candidates():
    primes = [p for p in eratosthenes_sieve(9999) if p > 1000]
    result = []

    for p in primes:
        for offset in range(1000, 4500, 2):
            if p + offset in primes:
                if sort_num(p) == sort_num(p + offset):
                    if p + 2 * offset in primes:
                        if sort_num(p) == sort_num(p + 2 * offset):
                            result.append([p, p + offset, p + 2 * offset])

    return result


def sort_num(num):
    return ''.join(sorted(str(num)))


print(evaluate_candidates())
