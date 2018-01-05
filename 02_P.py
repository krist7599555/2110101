# 02_P1
nm = int(input())
s1 = 'zero' if nm == 0 else 'negative' if nm < 0 else 'positive'
s2 = 'even' if nm % 2 == 0 else 'odd'
print(s1, s2)

# 02_P2
nm = float(input())
if nm < 0 or nm > 100:
	print('ERROR')
elif nm < 50:
	print('F')
else:
	nm -= 50
	for g in ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D'][::-1]:
		nm -= 5
		if nm < 0:
			print(g)
			break
	else:
		print('A')
    
# 02_P3
ls = sorted(map(float, input().split()))
print ('YES' if ls[0] + ls[1] > ls[2] else 'NO')

# 02_P4
from math import ceil
s = tuple(int(input()) for _ in range(2))
t = tuple(int(input()) for _ in range(2))
m = t[1] - s[1] + 60 * (t[0] - s[0])
if m <= 15:
	pay = 0
else:
	h = ceil(m / 60)
	if   h <= 3: pay = h * 10
	elif h <= 6: pay = 30 + 20 * (h - 3)
	else: pay = 200
print(pay)

# 02_P5
mny = float(input())
s1 = input().strip()
s2 = input().strip()
dis = {'NN':0, 'YN':5, 'NY':10, 'YY':20}[s1 + s2]
print(mny * (100 - dis) / 100)

# 02_P6
p1 = tuple(map(float, input().split()))
p2 = tuple(map(float, input().split()))
mat = [[i * j for j in p2] for i in p1]
slp = (mat[0][1] == mat[1][0])
cod = (mat[1][2] == mat[2][1])
if not p1[1] and not p2[1]: # special vertical
  spi = (mat[2][0] == mat[0][2])
	print(['no solution', 'many solutions'][spi])
else:
	tab = [['one', 'one'], ['no', 'many']]
	print(tab[slp][cod], 'solution' + ' s'[slp & cod])

# 02_P7
tax = [(1e5, .05), (4e5, .1), (5e5, .2), (3e6, .3), (float('inf'), .37)]
nm = float(input())
py = 0
for bn, pc in tax:
	hv = min(bn, nm)
	py += hv * pc
	nm -= hv 
print(py)

# 02_P8
x = (int(input()) - 543)
print (29 if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0) else 28)

# 02_P9
m, y = map(int, input().split())
y -= 543
mnt = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mnt[1] = 29 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 28
print(mnt[m-1])

# 02_P10
d, m, y = map(int, input().split())
if m < 3:
	m += 12
	y -= 1
c = y // 100
k = y % 100
w = d + (26 * (m + 1)) // 10 + k + k //4 + c // 4 + 5 * c
print(['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI'][w % 7])

# 02_P11
from math import hypot, fabs
x1, y1, r1, x2, y2, r2 = map(float, input().split())
dif = hypot(x1 - x2, y1 - y2) - r1 - r2
print (1 if fabs(dif) <= 1e-5 else 2 if dif < 0 else 3)

# 02_P12
h1, w1 = map(int, input().split())
h2, w2 = map(int, input().split())
mn = min(w1, h2 - w2)
print(w1 - mn, w2 + mn)
