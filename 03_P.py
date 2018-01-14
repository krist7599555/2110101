# 03_P1
from operator  import mul
from functools import reduce
def fac(n): return reduce(mul, range(1, n + 1))
print(fac(int(input())))

# 03_P2
from operator  import mul
from functools import reduce
def fac(n): return reduce(mul, range(1, n + 1))
n, k, cm = map(int, input().split())
print (fac(n) // fac(n-k) // fac(1 if cm == 1 else k))

# 03_P3
print(sum(i for i in range(int(input())) if not i % 3 or not i % 5))

# 03_P4
n = int(input())
print(sum(float(input()) for _ in range(n)) / n if n else 'No Data')

# 03_P5
ls = []
while True:
	vl = float(input())
	if vl != -1: ls.append(vl)
	else: break;
print(sum(ls) / len(ls) if ls else 'No Data')

# 03_P6
def grade(sc):
	lm_ = [50, 55, 60, 65, 70, 75, 80, 101]
	gd_ = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
	return next((gd for lm, gd in zip(lm_, gd_) if sc < lm), 'Error')
while True:
	sc = int(input())
	if sc != -1: print(grade(sc))
	else: break
  
# 03_P7
n, fnd = map(int, input().split())
print([int(input()) for _ in range(n)].count(fnd))

# 03_P8
import sys
vl = int(input())
for i in range(vl // 2, 1, -1):
	for j in range(min(i, vl - i) - 1, 1, -1):
		k = vl - i - j
		if k > j: break
		if i ** 2 == j ** 2 + k ** 2:
			print(i)
			sys.exit(0)
      
# 03_P9
from itertools import count
a, b, c, x, d = map(float, input().split())
f = lambda x: a * pow(x, 2) + b * x + c
f_= lambda x: a * x * 2 + b
for i in count(1):
	nw_x = x - f(x) / f_(x)
	if abs(nw_x - x) <= d:
		print(i)
		break
	else: x = nw_x

# 03_P10
n = int(input())
l = [i for i in range(2, n) if not n % i]
if l: print(*l[::-1])
else: print('Prime Number')

# 03_P11
vl = int(input())
if   vl < 0: print('input unavailable')
elif vl < 2: print('none')
else: print(*[i for i in range(2, vl + 1) 
   if all(i % j for j in range(2, i))])

# 03_P12
vl = int(input())
ls = []
for i in range(2, vl + 1):
	if not vl % i:
		ls.append(i)
		while not vl % i:
			vl //= i
print(*ls)

# 03_P13
r, c = map(int, input().split())
for i in range(1, r + 1):
	print(*(i * j for j in range(1, c + 1)))

# 03_P14
from operator import le, ge
n, cm = map(int, input().split())
func = [None, le, ge, lambda i, j: i + j == n - 1][cm]
print(*["({},{})".format(i + 1, j + 1) 
	for i in range(n) 
	for j in range(n) 
		if func(i, j)], sep = '\n')

# 03_P15
n = int(input()); x = n // 2 - 1; z = n // 2 - n; y = (n & ~1) - 1
f = lambda i, j: '#' if i+j>=x and i-j<y and i-j>=z else '.'
for i in range(n + y):
	ls = [f(i, j) for j in range(n + 1)]
	print(*ls[:-1], *ls[::-1], sep = '')

# 03_P16
x = int(input())
y = int(input())
for i in range(1, y + 1):
	print(x, i, x * i)
  
