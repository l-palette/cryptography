"""
3. Вычислить функцию Эйлера от следующих чисел:
а) 19;	б) 42;	в) 37;	г) 51;	д) 56;	 е) 127;   ж) 4451;   з) 730;  и) 87366.
"""

from helpers.euler import phi
from sympy import totient


def test():
    tests = [19, 42, 37, 51, 56, 127, 4451, 730, 87366]
    for i in range(len(tests)):
        assert totient(tests[i]) == phi(tests[i])
        print("-" * 40)


test()
