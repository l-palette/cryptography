from helpers.log import print_division
from helpers.log import pretty_print


class Result:
    def __init__(self, nod: int, iterations: list):
        self.nod = nod
        self.iterations = iterations


def binary_euclid(a: int, b: int, nod: int):
    init_a, init_b, init_nod = a, b, nod
    power_a, power_b = 0, 0
    while (a & 1) == 0 and (b & 1) == 0:
        a //= 2
        b //= 2
        nod *= 2

        power_a += 1
        power_b += 1

    while (a & 1) == 0:
        a //= 2
        power_a += 1

    while (b & 1) == 0:
        b //= 2
        power_b += 1

    if b > a:
        a, b = b, a
        init_a, init_b = init_b, init_a
        power_a, power_b = power_b, power_a

    nod_changed = False
    factoring_log = ""
    if a != init_a:
        factoring_log += (
            f"{init_a} / 2^{power_a} -> {a}\n"
            if power_a != 1
            else f"{init_a} / 2 -> {a}\n"
        )
        nod_changed = True
    if b != init_b:
        factoring_log += (
            f"{init_b} / 2^{power_b} -> {b}\n"
            if power_b != 1
            else f"{init_b} / 2 -> {b}\n"
        )
        nod_changed = True
    if nod_changed:
        factoring_log += f"nod: {init_nod} -> {nod}"
        pretty_print(factoring_log, grid="grid")
    return a, b, nod


def euclid(a: int, b: int, binary=True, comment=False) -> int:
    if comment:
        if binary:
            pretty_print("Бинарный алгоритм Евклида")
        else:
            pretty_print("Алгоритм Евклида")

    pretty_print(f"  gcd({a}, {b}) = ?", grid="fancy_grid")
    init_a, init_b = a, b
    nod = 1

    if binary:
        a, b, nod = binary_euclid(a, b, nod)

    if b > a:
        a, b = b, a

    iterations = [('abacaba')]
    remainder = a % b
    quotient = a // b

    while remainder > 0:
        iterations.append(('abacaba'))

        print_division(a, b, quotient, remainder)
        a, b = b, remainder
        if binary:
            a, b, nod = binary_euclid(a, b, nod)
        remainder = a % b
        quotient = a // b

    print_division(a, b, quotient, remainder)
    nod *= b

    if nod == 1:
        pretty_print(
            f"  gcd({init_a}, {init_b}) = {nod}, числа взаимно-простые",
            grid="fancy_grid",
        )
    else:
        pretty_print(
            f"  gcd({init_a}, {init_b}) = {nod}, числа не взаимно-простые",
            grid="fancy_grid",
        )

    result = Result(nod=nod, iterations=iterations)
    return result
