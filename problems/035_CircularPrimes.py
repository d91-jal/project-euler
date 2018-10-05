__author__ = 'johan'

from ProjectEuler.utils.primes import eratosthenes_sieve

# primes = eratosthenes_sieve(1000000)


def rotate_number(num):
    if num < 10:
        return num

    txt = str(num)
    return int(txt[-1] + txt[:-1])


# print(rotate_number(1))
# print(rotate_number(12345))


def find_circular_primes(upper):
    result = []
    primes = [i for i in eratosthenes_sieve(upper)]
    prime_arr = {i: True for i in primes}
    # print(primes)

    for i in primes:
        if i > upper:
            break

        temp = i
        is_prime = True

        for j in range(len(str(i)) - 1):
            temp = rotate_number(temp)
            is_prime = is_prime and prime_arr.get(temp)

            if not is_prime:
                break

        if is_prime:
            result.append(i)

    return result


# print(find_circular_primes(200))
a = find_circular_primes(1000000)
print(len(a), a)


