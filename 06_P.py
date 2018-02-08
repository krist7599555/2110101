# 06_P1
ls = []
while True:
	n = int(input())
	if n >= 0: ls.append(n)
	else: break
print(*map(n.__add__, ls), sep='\n')

# 06_P2
ls = [int(input()) for _ in range(int(input()))]
i, j = map(int, input().split())
print(sum(ls[i:j+1]))

# 06_P3
n = int(input())
print(sum(map(int, input().split())) / n)

# 06_P4
n = list(map(int, input().split()))
x = n.index(-1)
print(sum(n[:x]) / x)

# 06_P5
for ln in map(str.split, __import__('sys').stdin):
	if len(ln) != 2: break
	a, b = map(float, ln)
	print(a / pow(b * 1e-2, 2))

# 06_P6
ls = list(map(int, input().split()))
for i in range(len(ls)):
	m = ls[max(0, i-1): min(i+2, len(ls))]
	print(sum(m) // len(m), end=' ')

# 06_P7
a, b = [map(int, l.strip()[1:-1].split(',')) for l in [input(), input()]]
print(sum(map(int.__mul__, a, b)))

# 06_P8
ls = list(range(1, int(input()) + 1))
while True:
	a, b = map(int, input().split())
	if a == b == 0: break
	i, j = map(ls.index, [a, b])
	ls[i], ls[j] = ls[j], ls[i]
print(ls)

# 06_P9
s = input().split()
print(*map(lambda i: s[int(i)], input().split()))

# 06_P10
from itertools import groupby
print(sum(x for x, _ in groupby(input().split(','), key=lambda i: '-' in i)))

# 06_P11
ls = list(map(int, input().split()))
ls = [ls.pop((-1, 0)[ls[0] > ls[-1]]) for _ in range(len(ls))]
a, b = map(sum, [ls[::2], ls[1::2]])
print(a, b, [a == b, a > b, b > a].index(True))

# 06_P2
ls = list(input().strip())
for _ in range(int(input())):
	cm, *tp = input().split()
	if   cm == 'in'  :	ls.insert(int(tp[1]), tp[0])
	elif cm == 'out' : 	ls.pop(int(tp[0]))
	elif cm == 'swap':	
		i, j = map(int, tp)
		ls[i], ls[j] = ls[j], ls[i]
	print(*ls, sep='')

# 06_P13
dc = {i + 1: int(input()) for i in range(int(input()))}
it = 1
while True:
	print(it, end=' ')
	it = dc[it]
	if it == 1: break

# 06_P14
ls = []
for ln in map(str.strip, __import__('sys').stdin):
	cm, it, *_ = [*ln.split(None, 1), None]
	try:
		if cm == 'end': break
		print({
			'list'	:lambda: ls,
			'top'	  :lambda: ls[-1],
			'shelf'	:lambda: ls.pop(),
			'return':lambda: ls.append(it) or len(ls),
		}[cm]())
	except:
		print('no book')
