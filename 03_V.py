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
from math import factorial
def a(x, k):
    return pow(-1, k) * pow(x, 2 * k) / factorial(2 * k)
x, k = float(input()), 0
while abs(a(x, k)) > 1e-8:
    k += 1
print(sum(a(x, i) for i in range(k)), k-1)
