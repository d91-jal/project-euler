# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

from ProjectEuler.utils.primes import eratosthenes_sieve
from ProjectEuler.utils.utils import sort_as_string


def evaluate_candidates():
    primes = [p for p in eratosthenes_sieve(9999) if p > 1000]
    result = []
    counter = 0

    for p in primes:
        sorted_p = sort_as_string(p)

        for offset in range(1000, 4500, 2):
            counter += 1
            x1 = p + offset
            x2 = p + (2 * offset)

            if x2 > 9999:
                break

            if x1 in primes:
                if sorted_p == sort_as_string(x1):
                    if x2 in primes:
                        if sorted_p == sort_as_string(x2):
                            result.append([p, x1, x2])

    print(counter)
    return result


# Group all primes in the search space by their character content, and check if
# any group fulfills the given requirement of having three primes differing by
# the same amount. Note that each group may consist of more than three candidates.
def minimize_search_space_first():
    primes = [p for p in eratosthenes_sieve(9999) if p > 1000]
    prime_permutations = {}

    for p in primes:
        key = sort_as_string(p)

        if key not in prime_permutations:
            prime_permutations[key] = [p]
        else:
            prime_permutations[key].append(p)

    for x, y in prime_permutations.items():
        if len(y) >= 3:

            # Check if there are three items with the same offset in the current tuple.
            # TODO: This should be possible to do with a map/reduce construct.
            for i in range(0, len(y)-2):
                for j in range(i+1, len(y)-1):
                    offset = y[j] - y[i]

                    if y[j] + offset in y:
                        print(y[i], y[j], y[j] + offset)


minimize_search_space_first()
# print(evaluate_candidates())
