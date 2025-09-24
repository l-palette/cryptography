"""
2. Определить, являются ли числа a, b, c взаимно простыми? Попарно простыми?
а) a=32, b=43, c=65;	б) a=91, b=82, c=73; 		в) a=72, b=83, c=93.
---
Найти НОД (a,b), (b,c), (c,a). Если НОД хотя бы одной пары = 1, то числа взаимно простые
"""

from math import gcd
from tabulate import tabulate
from helpers.alphabet import russian_alphabet
from helpers.log import pretty_print
from helpers.euclid import euclid

def test():
    tests = [(32, 43, 65), (91, 82, 73), (72, 83, 93)]
    for i in range(len(tests)):
        print(f'{russian_alphabet[i]})')
        a, b, c = tests[i]

        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        pretty_print(f'gcd({a},{b},{c}) = ?')

        pairs = [(a, b), (b,c), (a,c)]
        gcds = []
        for first,second in pairs:
            cur_gcd = euclid(first, second).nod
            assert cur_gcd == gcd(first, second)
            gcds.append(str(cur_gcd))

        pretty_print('gcds = ' + (', '.join(gcds)))

        if any(cur_gcd == '1' for cur_gcd in gcds):
            pretty_print(f'gcd({a}, {b}, {c}) = 1, числа взаимно-простые')
        else:
            double_nod = euclid(int(gcds[0]), c).nod
            assert double_nod == gcd(a, b, c)
            pretty_print(f'gcd({a}, {b}, {c}) = {double_nod}, числа не взаимно-простые')

test()



