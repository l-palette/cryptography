from math import log
from helpers.log import pretty_print


def asymptotic(n: int) -> int:
    """
    :param n: last range num
    :return: approximate number of primes before n
    """
    if n < 2:
        return 0
    logarithm =  log(n)
    result = n / logarithm
    pretty_print(f'{n} / log({n}) = {round(result, 2)}', grid="simple_grid")
    return result


def eratosphen(n: int) -> list:
    """
    :param n: last range num
    :return: list is_prime of whether number is prime before n
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime


def naive(a: int, b: int) -> int:
    """
    :param a: first range num
    :param b: last range num
    :return: count of primes between a and b
    """
    is_prime = eratosphen(b)
    count = 0
    for i in range(a, b):
        if is_prime[i]:
            count += 1

    return count


