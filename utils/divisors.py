__author__ = 'johan'


def iter_divisors(max_size=10000):
    """iter_divisors
    Iterator over divisors of a number:

        for number, divisors in enumerate(iter_divisors()):
            print number, divisors

        This function yields integer arrays that are the divisors of any given
        number. It uses a method inspired by the sieve of Eratosthenes and it's
        quite fast. It runs in O(max_size) to find all divisors for all numbers
        less or equal to max_size.
    """
    divisors = []
    while len(divisors) < max_size + 1:
        divisors.append([])

    # 0 has no divider
    yield divisors[0]
    number = 1

    while number <= max_size:
        multiple = number

        while multiple <= max_size:
            divisors[multiple].append(number)
            multiple += number

        yield divisors[number]
        number += 1
