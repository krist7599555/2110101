# 60_1_Q1_2a_p
from math import sqrt
def P():
	return round(sqrt(7 + sqrt(6 + sqrt(5))), 6)
def R():
	n = int(input())
	sm = sum(sqrt(12) * pow(-3, -k) / (2 * k + 1) for k in range(n + 1))
	return round(sm, 12)
def S():
	m = int(input())
	q, r, t, k, n, x, i, p = 1, 0, 1, 1, 3, 3, 0, ''
	while i < m:
		if 4 * q + r - t < n * t:
			p += str(n)
			i += 1
			a = 10 * (r - n * t)
			n = 10 * (3 * q + r) // t - 10 * n
			q *= 10
			r = a
		else:
			a = (2 * q + r) * x
			b = (7 + q * k + x * r + 2) // (x * t)
			q *= k; t *= x
			x += 2; k += 1
			n, r = b, a
	return p[0] + '.' + p[1:]
f = globals().get(input().strip(), None)
print('pi = {}'.format(f()) if f else 'Invalid')

# 60_1_Q1_3a_p
import sys
sys.stdin = open(input().strip())
def conv(dc, mjoin, msep):
	for ls in map(str.strip, sys.stdin):
		try:    print(mjoin(map(dc.get, msep(ls))))
		except:	print('Invalid :', ls)
try:
	op = input().strip()
	dc = list(map(lambda l: l.split(']'), filter(bool, input().split('['))))
	conv(*{
		'M2T': [dict(dc), ''.join, str.split],
		'T2M': [dict({j: i for i, j in dc}), ' '.join, list]
	}[op])
except:
	print('Invalid code')

# 60_1_Q1_4a_p
inp = input().strip()			
s = ['10' if c == 'X' else c for c in list(inp)]
for i in range(1, len(s)):
	if s[i] == '/':
		s[i] = 10 - int(s[i-1])
s = list(map(int, s))
i = 0
ls = []
while i < len(s):
	a, b, c, *_ = s[i:i+3] + [0, 0, 0]
	sm = None
	if a == 10:
		sm = a + b + c
		i += 1
	elif a + b == 10:
		sm = a + b + c
		i += 2
	else:
		sm = a + b
		i += 2
	ls.append(sm)
try:
	nm = int(input())
	assert 1 <= nm <= 10
	print(ls[nm-1])
except:
	print(sum(ls[:10]))

