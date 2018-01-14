# 03_V1
print(['a', 'p', 'j', 'rs', 'v'][int(input()) - 1])

# 03_V2
sm = 0
while True:
	vl = int(input())
	if vl == -1: break
	if not vl % 2: sm += vl
print(sm)

# 03_V3
from math import ceil, sqrt
n = int(input())
s = dict({i * i : i for i in range(ceil(sqrt(n)) + 1)})
ls = []
for sq in s:
	tm = n - sq
	if 0 <= tm <= sq and tm in s:
		ls.append((s[tm], s[sq]))
for i, j in sorted(ls): print(i, j)
if not ls: print('No solution')

# 03_V4
from functools import reduce
from itertools import count
from operator  import mul
x = float(input())
mmo = 0
for k in count(0):
	tmp = pow(-1, k) * pow(x, 2 * k) / reduce(mul, range(1, 2 * k + 1), 1)
	if abs(tmp) < 1e-8:
		print(mmo, k - 1)
		break
	else:
		mmo += tmp
