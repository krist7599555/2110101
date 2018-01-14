# 03_L1
print(['a', 'v', 'n', 'p', 'efghijklmv'][int(input())-1])

# 03_L2
from itertools import count
from operator  import mul
s = list(map(int, input().strip()))
print(sum(map(mul, s[::-1], (2 ** i for i in count(0)))))

# 03_L3
nm, bs = map(int, input().split())
if 0 < nm and 1 < bs < 10:
	ls = []
	while nm:
		ls.append(nm % bs)
		nm //= bs
	print(*ls[::-1], sep='')
else:
	print('Error: Cannot convert' if nm != 0 else '0')

# 03_L4
n = int(input())
print(sum(j*j*(j+1)//2 for j in range(n&1, n+1, 2)) * [1,-1][n&1])
