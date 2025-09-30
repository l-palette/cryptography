"""
10. Решить сравнения
а)11x≡18(mod31);	 б)25x≡30(mod 55);	 в)14x≡21(mod 31);	г)12x≡19(mod81).
"""
from helpers.euclid import euclid
from helpers.log import pretty_print
from helpers.alphabet import russian_alphabet
tests = [(11, 18, 31), (5, 6, 11), (2, 3, 31), (12, 19, 81)]
for i in range(len(tests)):
    a, b, mod = tests[i]
    print(f"{russian_alphabet[i]}) {a}x ≡ {b} (mod {mod})")
    for x in range(-mod, mod + 1):
        if a * x % mod == b:
            pretty_print(f'X = {x}')
    result = euclid(a, mod, binary=False)
    nod = result.nod
    if nod != 1:
         pretty_print("Обратного не существует")
    else:
        print(f"{pow(a, -1, mod)=}")
        print(f"{pow(a, mod - 2, mod)=}")
