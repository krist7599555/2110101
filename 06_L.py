# 06_L1
print('cbbdc'[int(input()) - 1])

# 06_L2
l = [int(i) & 1 for i in input().split()]
print(l, sum(l), sep='\n')

# 06_L3
def check(l):
	d = list(map(int.__sub__, l[1:], l))
	return len(set(d)) == 1 and l[-1] + d[0]
ls = list(map(int, input().split()))
print(check(ls) or check(ls[slice(len(ls) & 1, None, 2)]))

# 06_L4
mat = [list(map(int, s.split())) for s in __import__('sys').stdin][::-1]
print(sum(sum(mat[x][x: len(mat[0]) - x]) for x in range(len(mat))))
