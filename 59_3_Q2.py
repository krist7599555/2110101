# 59_3_Q2_2_p
def A():
	m, p, q = [int(input()) for _ in range(3)]
	for i in range(m + 1):
		for j in range(p):
			if i + j > q:
				print('P3', i, j)
				break
		else:
			print('P4', i, j)
def B():
	m, p = [int(input()) for _ in range(2)]
	i, c = 0, 0
	while i <= m:
		j = i
		while j <= p:
			print(i, j)
			c += 1
			j += 1
		i += 1
	print(c)
globals().get(input().strip(), lambda: print('Invalid op'))()

# 59_3_Q2_3_p
def solve(dna, cmd):
	if set(dna) - set('ATCG'):
		return 'Invalid DNA'
	elif cmd == 'R':
		dic = dict(zip('ATCG', 'TAGC'))
		return ''.join(map(dic.get, dna))[::-1]
	elif cmd == 'F':
		dic = dict(__import__('collections').Counter(dna))
		return ', '.join('{}={}'.format(c, dic.get(c, 0)) for c in 'ATGC')
	elif cmd == 'D':
		pii = tuple(input().strip().upper())
		return list(zip(dna, dna[1:])).count(pii)
dna = input().strip().upper()
cmd = input().strip()
print(solve(dna, cmd))

# 59_3_Q2_4_p
def flip(mat): return [ls[::-1] for ls in mat]
def ro90(mat): return flip(''.join(flip(s)) for s in zip(*mat))
deg = input().strip()
mat = [input().strip() for _ in range(int(input()))]
if len(set(map(len, mat))) != 1:
	print('Invalid size')
else:
	try:
		for _ in range(int(deg) // 90):
			mat = ro90(mat)
	except:
		mat = flip(mat)
	print(*mat, sep='\n')
