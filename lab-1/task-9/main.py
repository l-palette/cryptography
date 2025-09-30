"""
9. Вычислить a^{-1} mod b, если таковой существует, где
а) a=23, b=72;	б) a=5, b=43;	в) a=9, b=17;	г) a=39, b=73.
---
НОД(a,b) = 1?
"""

from helpers.euclid import euclid
from helpers.log import pretty_print
from helpers.alphabet import russian_alphabet



tests = [(23, 72), (5, 43), (9, 17), (39, 73)]
for i, (a, b) in enumerate(tests):
    print(f"{russian_alphabet[i]}) a = {a}, b = {b}")
    result = euclid(a,b, binary=False)
    nod = result.nod
    if nod != 1:
         pretty_print("Обратного не существует")
    else:
        print(f"{pow(a, -1, b)=}")
        print(f"{pow(a, b - 2, b)=}")