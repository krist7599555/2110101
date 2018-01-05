# 01_P1
from operator import *
a = int(input())
b = int(input())
print(*[f(a, b) for f in [add, sub, mul, truediv, floordiv, mod, pow]], sep='\n')

# 01_P2
from math import pi
print(pi * pow(float(input()), 2))

# 01_P3
print(sum(float(input()) for _ in range(5)) / 5)

# 01_P4
from math import factorial
x = float(input())
ls = [pow(x, i) / factorial(i) for i in range(5)]
print(*ls[2:], sum(ls), sep='\n')

# 01_P5
a, b, c = tuple(float(input()) for _ in range(3))
x = pow(pow(b,2) - 4 * a * c, .5)
print("x1 = ", (-b+x) / (2*a))
print("x2 = ", (-b-x) / (2*a))

# 01_P6
a1, b1, c1 = map(float, input().split())
a2, b2, c2 = map(float, input().split())
cal_x = lambda : (b1 * c2 - b2 * c1) / (b2 * a1 - a2 * b1)
print(cal_x(), end=' ')
a1, b1 = b1, a1
a2, b2 = b2, a2
print(cal_x())

# 01_P7
c = float(input())
print(9 / 5 * c + 32, c + 273.15)

# 01_P8
w = float(input())
h = float(input()) / 100
print(w / h ** 2)

# 01_P9
a, b, c = map(float, input().split())
p = (a + b + c) / 2
print(pow(p * (p - a) * (p - b) * (p - c), 0.5))

# 01_P10
from operator import mul
nm = list(map(int, input()))
sm = sum(map(mul, reversed(range(11)), nm)) % 11
print (*nm, (11 - sm) % 11, sep='')
