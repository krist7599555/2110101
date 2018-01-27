# 05_P1
grade = lambda cs: next(j for i, j in list(zip([0, 50, 55, 60, 65, 70, 75, 80], "F D D+ C C+ B B+ A".split()))[::-1] if cs >= i)
for s in map(str.split, open(input().strip())):
	print(s[0], grade(sum(map(int, s[1:]))))

# 05_P2
grade = lambda cs: next(j for i, j in list(zip([0, 50, 55, 60, 65, 70, 75, 80], "F D D+ C C+ B B+ A".split()))[::-1] if cs >= i)
cin = iter(open(input().strip()))
for _ in range(int(next(cin))):
	nm, *sc = next(cin).split()
	print(nm, grade(sum(map(int, sc))))

# 05_P3
print(dict(map(str.split, open('score.txt'))).get(input().strip(), 'Not Found'))

# 05_P4
dic = {'BE':0, 'SE':1, 'VE':2, 'ET':3}
cnt = [0, 0, 0, 0]
for s in open(input().strip()):
	try: cnt[dic[s.upper().split()[0]]] += 1
	except: pass
print(*cnt, sum(cnt))

# 05_P5
print(*(('False', 'True')[j in i] for i, j in zip(open(input().strip()), map(str.strip, open(input().strip())))), sep='\n')

# 05_P6
from itertools import islice
f1, f2 = tuple(open(input().strip()) for _ in range(2))
it = iter(map(float, f2))
for n in map(int, f1):
	print(sum(islice(it, n)) / n)

# 05_P7
print(sum(1 for ln in open(input().strip()) if not ln.strip()))

# 05_P8
import sys
sys.stdin = open(input().strip())
func = getattr(str, input().strip())
q = input().strip()
for w, s, t in map(lambda s: s.strip().split(), sys.stdin):
	x = func(w, q, int(s), int(t))
	print(w[max(0, x - 1): x + len(q) + 1] if x != -1 else 'not found')
