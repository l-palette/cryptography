"""
7. Выписать полную и приведенную системы наименьших неотрицательных вычетов по следующим модулям:
а) 5;		б) 8;		в) 10;		г) 15;		д) 18;		е) 20.
---
Приведенная система вычетов по модулю m — это набор чисел, взаимно простых с m, которые не сравнимы по модулю m друг с другом.
В приведенной системе вычетов содержится ровно φ(m) (функция Эйлера) чисел
"""

from helpers.euler import phi
from helpers.remainder_systems import reduced_remainder_system, full_remainder_system


tests = [5, 8, 10, 15, 18, 20]


for modulus in tests:
    full_system = full_remainder_system(modulus)
    reduced_system = reduced_remainder_system(modulus)

    print(f"Модуль {modulus}:")
    print(f"Полная система: {full_system}")
    print(f"Приведенная система: {reduced_system}")
    print(f"Количество элементов в приведенной системе: {phi(modulus)}")
    print()