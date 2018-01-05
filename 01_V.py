# 01_V1
print('ebebb'[int(input()) - 1])

# 01_V2
from math import sin, pi
a = float(input())
b = float(input())
c = float(input())
print("area = {} (sq cm)".format(.5 * a * b * sin(c / 180 * pi)))

# 01_V3
from operator import sub
t1 = tuple(int(input()) for _ in range(3))
t2 = tuple(int(input()) for _ in range(3))
df = list(map(sub, t2, t1))
for i in [2, 1]:
	if df[i] < 0:
		df[i] += 60
		df[i-1] -= 1
print(*df, sep=':')

# 01_V4
from math import log10
w = float(input())
h = float(input())
print(
 pow(w * h, .5) / 60,
 .024265 * pow(w, .5378) * pow(h, .3964),
 .033300 * pow(w, .6157 - .0188 * log10(w)) * pow(h, .3),
 sep = '\n')
