
# 01_L1
print('beebd'[int(input())-1])

# 01_L2
from math import sqrt, cos, radians
a, b, c = tuple(float(input()) for _ in range(3))
print("c = {} cm.".format(sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b * cos(radians(c)))))

# 01_L3
from operator import sub
t1 = tuple(int(input()) for _ in range(3))
t2 = tuple(int(input()) for _ in range(3))
df = list(map(sub, t2, t1))
for i in [2, 1]:
	if df[i] < 0:
		df[i] += 60
		df[i-1] -= 1
if df[0] < 0:
	df[0] += 24
print(*df, sep=':')

# 01_L4
from operator import mul
print((11 - sum(map(mul, map(int, input()), range(13, 0, -1))) % 11) % 10)
