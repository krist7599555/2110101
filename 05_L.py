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
f = ''.join(open(input().strip()))
l = int(input())
s = input().strip('\n\r')
t = input().strip('\n\r')
i = 0
for _ in range(l):
	while i != len(f):
		if f[i: i + len(s)].lower() == s.lower():
			f = f[:i] + t + f[i + len(s):]
			i += 1
			break
		else:
			i += 1
print(f)

