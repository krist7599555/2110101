# 08_P1
lis = []
for _ in range(int(input())):
    user, city = input().strip().split(': ')
    lis.append([user, set(city.split(', '))])
fnd = input().strip()
vis = dict(lis).get(fnd)
ans = [usr for usr, city in lis if usr != fnd and city & vis]
print(*ans or ['Not Found'], sep='\n')

# 08_P2
from collections import defaultdict
dc = defaultdict(list)
for _ in range(int(input())):
	head, *tail = map(str.strip, input().split(', '))
	for i in tail:
		dc[i].append(head)
for q in map(str.strip, input().split(', ')):
	print(q, '->', ', '.join(dc.get(q, ['Not found'])))

# 08_P3	
from collections import Counter
print(min([vl for vl, cnt in Counter(map(int, input().split())).items() if cnt == 1], default='NONE'))

# 08_P4
inp = list(map(int, input().split()))
fnd = int(input())
cnt = 0
for i in range(len(inp)):
  for j in range(i):
    if inp[i] + inp[j] == fnd:
      cnt += 1
print(cnt)

# 08_P5
from collections import defaultdict
inp = map(int, input().split())
fnd = int(input())
cnt, dic = 0, defaultdict(int)
for val in inp:
    cnt += dic[fnd - val]
    dic[val] += 1
print(cnt)

# 08_P6
from collections import defaultdict
def solve(n, m, ls, qr):
    dc = defaultdict(list)
    for i in range(n):
        for x in range(m):
            dc[qr[x] - ls[i]].append((x, i))
    ok = ['NO'] * m
    for i in range(n):
        for j in range(i):
            for x, k in dc.get(ls[i] + ls[j], []):
                if len(set([i, j, k])) == 3:
                    ok[x] = 'YES'
    print(*ok, sep='\n')
n, m = map(int, input().split())
ls = list(map(int, input().split()))
qr = list(map(int, input().split()))
solve(n, m, ls, qr)

# 08_P7
from collections import defaultdict
n, d, mx = int(input()), defaultdict(list), 0
for _ in range(n):
	s = input().split('\t', 1)[1]
	d[s[:2]].append(s)
	mx = max(mx, len(d[s[:2]]))
k = next(k for k, v in sorted(d.items()) if len(v) == mx)
print(k, len(d[k]), *d[k], sep='\n')

# 08_P8
ls1, ls2 = map(str.split, [input(), input()])
cov = dict([*zip(ls1, ls2), *zip(ls2, ls1)])
print(*[cov.get(s, s) for s in input().split()])

# 08_P9
ls = [int(input()) for _ in range(int(input()))]
print(max(sorted(ls), key=ls.count))

# 08_P10
lis = sorted([input().split() for i in range(int(input()))])
fnd = [None] * 4
for tok in input().split():
	if   tok.isdigit():	fnd[2] = tok
	elif tok.isupper(): fnd[[3, 1][len(tok) == 1]] = tok
	elif tok.istitle():	fnd[tok == 'Dog'] = tok
ans = [' '.join(it) for it in lis if all(i is None or i == j for i, j in zip(fnd, it))]
print(*ans or ['Not Found'], sep='\n')

# 08_P11
from collections import Counter
from itertools import chain
lis = [set(input().split()) for _ in range(int(input()))]
fnd = input().strip()
lis = sorted((-j, i) for i, j in Counter(chain(*[l for l in lis if fnd in l])).items())
if   len(lis) == 0: print('Not Found')
elif len(lis) == 1: print('No suggested event')
else: print(lis[1][1], -lis[1][0], sep='\n')

# 08_P12
from collections import defaultdict
lis = [set(input().split()) for _ in range(int(input()))]
fnd = input().strip()
dic = defaultdict(int)
for st in lis:
	if fnd in st:
		for it in st:
			dic[it] += 1
ans = sorted(dic.items(), key=lambda t:[-t[1], t[0]])
if len(ans) > 1:
	for i, j in ans[1:]:
		print(i, j)
else: 
	print('No suggested event' if ans else 'Not Found')
	
# 08_P13
edge = __import__('collections').defaultdict(list)
while True:
	inp = input().strip()
	try:
		i, j = inp.split()
		edge[i].append(j)
		edge[j].append(i)
	except:
		ans = [inp]
		for u in edge[inp]:
			ans.append(u)
			ans.extend(edge[u])
		print(*sorted(set(ans)), sep='\n')
		break
		
# 08_P14
dc = dict()
for _ in range(int(input())):
	fc, lm = input().split()
	dc[fc] = int(lm)
ls = []
for _ in range(int(input())):
	nm, sc, *fc = input().split()
	ls.append([float(sc), nm, fc])
ans = []
for sc, nm, fc in sorted(ls, reverse=True):
	for it in fc:
		if dc.get(it):
			dc[it] -= 1
			ans.append('{} {}'.format(nm, it))
			break
print(*sorted(ans), sep='\n')

# 08_P15
m1, m2, m3 = [[ln.strip().split(',') for ln in open(input().strip())] for _ in range(3)]
m1, m2 = map(dict, [m1, m2])
for i, j in m3:
	try:    print(m1[i] + ',' + m2[j])
	except: print('record error')
	
# 08_P16	
lis = [set(map(int, input().split())) for _ in range(int(input()))]
try:
	print(len(set.union(*lis)))
	print(len(set.intersection(*lis)))
except:
	print(0, 0, sep='\n')
	
# 08_P17
team, loss = set(), set()
for _ in range(int(input())):
    a, b = input().split()
    team.add(a)
    loss.add(b)
print(sorted(team - loss))
