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
