"""
8. Верны ли следующие сравнения?
а) 2≡22(mod 10);	б) -14≡13(mod 9);	в) -15≡-11(mod 3);	г)21≡15(mod5).
"""

from helpers.alphabet import russian_alphabet
from helpers.log import bools_emoji, pretty_print


def check_correctness(a, b, mod):
    # Вычисляем коэффициенты и остатки
    quotient_a = a // mod
    std_remainder_a = a % mod

    quotient_b = b // mod
    std_remainder_b = b % mod

    # Выбираем остаток с наименьшим абсолютным значением
    remainder_a = std_remainder_a
    if std_remainder_a > mod / 2:
        remainder_a = std_remainder_a - mod
        quotient_a += 1

    remainder_b = std_remainder_b
    if std_remainder_b > mod / 2:
        remainder_b = std_remainder_b - mod
        quotient_b += 1  #

    is_correct = remainder_a == remainder_b

    print(f"    {remainder_a} ≡ {remainder_b} (mod {mod}): {'✓' if is_correct else '✗'}")

    if quotient_a:
        first_log = f"{a} = {mod} * {quotient_a} + {remainder_a}\n{a} - {mod * quotient_a} = {remainder_a}"
        pretty_print(first_log)

    if quotient_b:
        second_log = f"{b} = {mod} * {quotient_b} + {remainder_b}\n{b} - {mod * quotient_b} = {remainder_b}"
        pretty_print(second_log)

    return is_correct

tests = [(2, 22, 10), (-14, 13, 9), (-15, -11, 3), (21, 15, 5)]
for i in range(len(tests)):
    a, b, mod = tests[i]
    print(f"{russian_alphabet[i]}) {a} ≡ {b} (mod {mod})")
    check_correctness(a, b, mod)