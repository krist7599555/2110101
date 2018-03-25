# 08_L1
print('dbacd'[int(input()) - 1])

# 08_L2
import sys
dic = dict()
for ln in open('address.txt'):
    nme, tel = ln.rsplit(None, 1)
    dic[nme] = tel
    dic[tel] = nme
print(*[dic.get(ln.strip(), 'Not Found') for ln in sys.stdin if ln.strip()], sep='\n')

# 08_L3
from collections import Counter
ls = ''.join(c for c in ' '.join(open(input().strip())).lower() if c is ' ' or c.isdigit() or c.isalpha()).split()
print(sorted(Counter(ls).items(), key=lambda i: (-i[1], i[0]))[:10])

# 08_L4
from collections import defaultdict
from operator import itemgetter
dic = defaultdict(set)
for x, ln in enumerate(open('books.txt')):
	head, *tail = map(str.strip, ln.split(', '))
	for i in tail:
		dic[i].add((x, head))
ans = set.intersection(*[dic[i] for i in map(str.strip, input().split(', '))])
print(*map(itemgetter(1), sorted(ans)) if ans else ['Not found'], sep='\n')
