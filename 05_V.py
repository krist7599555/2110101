# 05_V1
print('abedd'[int(input()) - 1])

# 05_V2
from itertools import islice
f = map(str.strip, open('data.txt', 'r'))
l = list(ln[ln.find(' ') + 1:] for ln in islice(f, None, None, 4))
try:    print(l[int(input())-1])
except: print('Not Found')

# 05_V3
from itertools   import repeat
from collections import OrderedDict
mp = map(lambda s: s[:10], open(input().strip()))
print(*OrderedDict(zip(mp, repeat(None))).keys(), sep='\n')

# 05_V4
from collections import Counter
m = Counter(''.join(open(input().strip())))
s = ''.join(map(str.strip, [input(), input(), input()]))
print(*sorted(s, key=lambda c: m.get(c, 0), reverse = True), sep='')
