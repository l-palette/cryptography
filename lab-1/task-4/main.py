"""
4. Пользуясь асимптотическим законом распределения простых чисел,
вычислить примерное количество простых чисел в промежутке от 80000 до 120000.
---
Теорема о распределении простых чисел утверждает, что доля простых чисел среди чисел от 1 до n примерно равна 1/ ln(n)
Найдем значение простых чисел от 1 до 120000, затем от 1 до 80000 и вычтем
"""
from helpers.asymptotic import asymptotic
from helpers.asymptotic import naive

a, b = 80000, 120000
asymptotic1 = asymptotic(a)
asymptotic2 = asymptotic(b)
result = asymptotic2 - asymptotic1

print(f'Кол-во простых чисел по ТЗРП: {round(result, 2)}')
print(f'Кол-во простых чисел: {naive(a, b)}')