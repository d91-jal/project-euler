__author__ = 'johan'

# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def simple_solution(upper_bound):
    result = 0

    for i in range(0, upper_bound, 3):
        result += i

    for i in range(0, upper_bound, 5):
        if (i % 3) > 0:
            result += i

    return result


def sneaky_solution(upper_bound):
    base = [3, 5, 6, 9, 10, 12, 15]
    new = [0]
    i = 0

    while i * 15 < upper_bound:
        for j in base:
            next_mult = (15 * i) + j

            if next_mult < upper_bound:
                new.append(next_mult)
            else:
                break

        i += 1
        # print(new)

    return sum(new)


print(simple_solution(1000))
print(sneaky_solution(1000))


