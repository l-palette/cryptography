"""
11. Решить системы сравнений
а)
9x≡1(mod 11)
2x≡1(mod 3)
б)
5x≡2(mod 9)
3x≡2(mod 7)
в)
8x≡5(mod 11)
3x≡2(mod 5)
г)
11x≡7(mod 13)
4x≡5(mod 7)
д)
8x≡3(mod 9)
4x≡1(mod 5)
7x≡1(mod 8)
е)
4x≡1(mod 5)
3x≡5(mod 7)
5x≡8(mod 11)
ж)
x≡(4^{-1})(mod 9)
5x≡7(mod 10)
11x≡7(mod 19)
з)
x≡7(mod 11)
32x≡21(mod 71)
3x≡2(mod 4)
"""

def gcdex(a, b):
	if b == 0:
		return a, 1, 0
	else:
		d, x, y = gcdex(b, a % b)
		return d, y, x - (a // b) * y

def kto(a1,a2,m1,m2):
	M = m1*m2
	M1 = m2
	M2 = m1
	print(f'{M1=}, {M2=}')
	o, M1_, o = gcdex(M1,m1)
	o, M2_, o = gcdex(M2,m2)
	print(f"{a1} * {M1} * {M1_} + {a2} * {M2} * {M2_} % {M}")
	x = (a1 * M1 * M1_ + a2 * M2 * M2_) % M
	return x


def kto3(a1,a2,a3, m1,m2, m3):
	M = m1 * m2 * m3
	M1 = m2 * m3
	M2 = m1 * m3
	M3 = m1 * m2
	print(f'{M1=}, {M2=}, {M3=}, {M=}')

	M1_ = pow(M1,-1, m1)
	M2_ = pow(M2, -1, m2)
	M3_ = pow(M3, -1, m3)


	print(f"{a1} * {M1} * {M1_} + {a2} * {M2} * {M2_} + {a3} * {M3} * {M3_} % {M}")
	x = (a1 * M1 * M1_ + a2 * M2 * M2_ + a3 * M3 * M3_) % M
	return x

tests = [(5, 2, 11, 3), (4, 10, 9, 7), (2, 4, 11, 5), (4, 6, 35, 11)]
for a1, a2, m1, m2 in tests:
	print(f'{a1=}, {a2=}, {m1=}, {m2=},')
	x = kto(a1, a2, m1, m2)
	print(f'{x=}')

tests3 = [(6, 4, 7, 9, 5, 8)]
for a1, a2, a3, m1, m2, m3 in tests3:
	print(f'{a1=}, {a2=}, {a3=}, {m1=}, {m2=}, {m3=}')
	x = kto3(a1, a2, a3, m1, m2, m3)
	print(f'{x=}')
