# 08_V1
print('ceedc'[int(input()) - 1])

# 08_V2
import re
f = [set(re.split('\W+', ''.join(open(f)).lower())) for f in ['file1.txt', 'file2.txt']]
s = input().strip().lower()
print({
  0b11: "Found in both files", 
  0b10: "Found in file1 only", 
  0b01: "Found in file2 only", 
  0b00: "Not found"
  }[(s in f[0]) * 2 + (s in f[1])])

# 08_V3  
import sys
dic = dict()
for ln in open('address.txt'):
    fnm, lnm, tel, mail = ln.split()
    dic[fnm + ' ' + lnm] = tel + ' ' + mail
print(*[dic.get(ln.strip(), 'Not found') for ln in sys.stdin if ln.strip()], sep='\n')

# 08_V4
from collections import defaultdict
dc = defaultdict(set)
while True:
	try:	room, stdnt = input().split(None, 1)
	except:	break
	for s in stdnt.split():
		dc[s].add(room)
a, b = map(dc.__getitem__, input().split())
print(*map(len, [a & b, a ^ b, a | b]))
