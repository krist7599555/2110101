# 05_L1
print('dcddd'[int(input()) - 1])

# 05_L2
dc = __import__('collections').defaultdict(list)
for ln in open('data.txt'):
	ky, vl = ln.strip().split(':')[-2:]
	dc[ky].append(float(vl))
it = dc.get(input().strip(), None)
print(sum(it)/len(it) if it is not None else 'Not Found')

# 05_L3
print(__import__('functools').reduce(int.__xor__, map(ord, ''.join(open(input().strip())))))

# 05_L4
f = map(str.strip, open(input().strip()))
n = int(input())
s = input().strip('\n\r')
t = input().strip('\n\r')
for ln in f:
	o, i = '', 0
	while i != len(ln):
		if n != 0 and ln[i:i+len(s)].lower() == s.lower():
			o += t 
			i += len(s)
			n -= 1
		else:
			o += ln[i]
			i += 1
	print(o)
