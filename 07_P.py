# 07_P1
s = input().strip()
print(*map(s.count, '0123456789'), sep='\n')

# 07_P2
from string import *
print(*map(input().count, digits + ascii_uppercase + ascii_lowercase))

# 07_P3
f = dict(map(str.split, open('score.txt')))
while True:
	x = input().strip()
	if x == '-1': break
	print(f.get(x, 'Not Found'))

# 07_P4
from itertools import count
from collections import defaultdict
dc = defaultdict(int)
for i in count():
	s = int(input())
	if s != -1: dc[s] += 1
	else: 	
		print(next((k for k, v in dc.items() if v > i / 2), 'Not found'))	
		break

# 07_P5
n = int(input()); 
print(*sorted([int(input()) for _ in range(n)], reverse=True), sep='\n')

# 07_P6
import numpy as np
ls = [int(input()) for _ in range(int(input()))]
print(np.mean(ls), np.median(ls), max(ls, key=ls.count))

# 07_P7
print(*sorted(s.split()[0] for s in open('score.txt')))

# 07_P8
print(*sorted((s.split()[0] for s in open('score.txt')), reverse=True))

# 07_P9
ls = [[], []]
for vl in map(int, input().split()):
  ls[vl & 1].append(vl)
print(*sorted(ls[0]), *sorted(ls[1], reverse=True))

# 07_P10
from operator import itemgetter
from bisect import *
n = int(input())
ls, cnt = [], 0
for _ in range(n):
    st = input().strip()
    ln = [len(st), st]
    xi = bisect_right(ls, ln)
    cnt += len(ls) - xi
    ls.insert(xi, ln)
print(*map(itemgetter(1), ls), cnt, sep='\n')

# 07_P11
import numpy as np
grade = dict(zip("A B+ B C+ C D+ D F".split(), [4, 3.5, 3, 2.5, 2., 1.5, 1, 0]))
r, c = map(int, input().split())
for _ in range(r):
	print(format(np.array([grade[g] for g in input().split() if g != 'X']).mean(), '.2f'))
	
# 07_P12
cmd, n = map(int, input().split())
print(sum(sum(list(map(int, input().split()))[
  [slice(None, i + 1), slice(i, None)][cmd]]) for i in range(n)))
 
# 07_P13
import numpy as np
r, c = map(int, [input(), input()])
ar = np.array([input().split() for _ in range(r)], dtype=np.int)
for i in range(r):
	for j in range(i):
		if (ar[i,:] == ar[j,:]).all():
			for v in [j, i]:
				print(v + 1)
				print(*ar[v])
				
# 07_P14
import numpy as np
import itertools
r, c = map(int, input().split())
ar = np.array([input().split() for _ in range(r)], dtype=np.int)
for i, j in itertools.product(range(r), range(c)):
	if min(ar[i,:]) == max(ar[:,j]) == ar[i, j]:
		print(ar[i, j])
		break
else:
	print(-1)

# 07_P15
import numpy as np
n = int(input())
m = np.array([input().split() for _ in range(n)], dtype=np.int)
print(next((i for i in range(n) if [m[i,:].sum(), m[:,i].sum()] == [1, n]), -1))

# 07_P16
r, c = map(int, input().split())
ls = [map(int, input().split()) for _ in range(2 * r)]
for i in range(r):
	print(*map(int.__add__, ls[i], ls[i+r]))
  
# 07_P17
ls = []
while True:
	ln = input().split()
	if len(ln) == 2:
		ls.append((float(ln[1]), int(ln[0])))
	else:
		ls.sort(key=lambda sc: (-sc[0], sc[1]))
		print(next((i for i, v in enumerate(ls, 1) if v[1] == int(ln[0])), 'Not Found'))
		break

# 07_P18	
from string import ascii_lowercase
s = [input().strip() for _ in range(int(input()))]
print('\n'.join(sorted(s, key=lambda it: [list(map(it.count, ascii_lowercase)), it])))
