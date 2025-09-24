"""
1. Вычислить НОД(a,b) двумя способами: алгоритмом Евклида с делением с остатком
и бинарным алгоритмом Евклида.
Сравнить количество итераций для этих алгоритмов.
а) a=88, b=34;	б) a=393, b=127;	в) a=232, b=791;	г) a=932, b=212.
---
Бинарный алгоритм Евклида означает сокращение на 2 и домножение НОДа на 2, если сокращаются обе переменные
"""
from math import gcd
from tabulate import tabulate
from helpers.alphabet import russian_alphabet
from helpers.euclid import euclid
from helpers.log import pretty_print


def test():
    tests = [(88, 34), (393, 127), (232, 791), (932, 212)]
    for i in range(len(tests)):
        print(f'{russian_alphabet[i]})')
        a, b = tests[i]
        euclid_result = euclid(a, b, binary=False, comment=True)
        binary_euclid_result = euclid(a,b, comment=True)

        pretty_print(f'euclid = {euclid_result.iterations} iterations, bin_euclid = {binary_euclid_result.iterations} iterations', grid="simple")
        assert euclid_result.nod == gcd(a, b)
        assert binary_euclid_result.nod == gcd(a, b)

test()



