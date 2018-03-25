# 07_V1
print('dadbe'[int(input()) - 1])

# 07_V2
m = map(int, input().split())
print(sorted(m, reverse = 'd' in input()))

# 07_V3
from operator import itemgetter
fnd = int(input())
data = []
for ln in open('hotels.txt'):
    h, s, v = ln.split(';')
    if int(s) >= fnd:
      data.append([h, int(s), float(v)])
data.sort(key=itemgetter(-1), reverse=True)
for tp in data or [["Not Found"]]: print(*tp)

# 07_V3
from operator import itemgetter
fnd = input().strip()
dat = [ln for ln in map(str.split, open('circulations.txt')) if ln[-1] < fnd]
dat = sorted(dat, key=itemgetter(-1))
print(*map(' '.join, dat) if dat else ['Not Found'], sep='\n')
