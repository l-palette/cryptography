from math import gcd


def full_remainder_system(mod):
    return list(range(mod))


def reduced_remainder_system(mod):
    return [i for i in range(1, mod) if gcd(i, mod) == 1]

