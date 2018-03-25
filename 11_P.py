# 11_P1
import numpy as np
data = np.array([[15,3.78],[29,2.00],[10,2.50],[25,2.85],[30,3.96]])
logistic = -3.98 + 0.2 * data[:,0] + 0.5 * data[:,1]
sigmoid  = 1 / (1 + np.exp(-logistic))
n = int(input())
print(bool(np.round(sigmoid[n-1])) if 1 <= n <= 5 else 'Error')

# 11_P2
import numpy as np
n = int(input())
a = np.array([input().split()[1] for _ in range(n)], dtype=np.float)
b = np.array([input().split()[1:]for _ in range(n)], dtype=np.float)
print(*np.dot(a, b), sep='\n')

# 11_P3
import numpy as np
for _ in range(int(input())):
    inp = input().split(',')
    if len(inp) == 7:
        try:    print(sum(map(float, inp[1:])))
        except: pass
        
# 11_P4        
import numpy as np
def fib(n, mod):
	fb = np.matrix([[0,1],[1,1]], dtype=np.int)
	nw = np.matrix([[1,0],[0,1]], dtype=np.int)
	for _ in range(n): 
	  nw = nw * fb % mod
	return nw[0, 1]
print(fib(*map(int, input().split())))

# 11_P5
import numpy as np
def fib(n, mod):
	return np.matrix(['1 0; 0 1', '0 1; 1 1'][n]) if n <= 1 \
		else fib(n // 2, mod) ** 2 * fib(n & 1, mod) % mod
print(fib(*map(int, input().split()))[0, 1])

# 11_P6
import numpy as np
r, c = map(int, input().split())
m = np.array([input().split() for _ in range(r)], dtype=np.int)
d = int(input())
for i in range(0, r, d):
	print(*[m[i:i+d, j:j+d].mean() for j in range(0, c, d)])
	
# 11_P7
import numpy as np
n = int(input())
m = np.array([input().split() for _ in range(n)], dtype=np.int)
assert (np.diag(m) == 1).all()
for ln in np.sign(np.linalg.matrix_power(m, len(m))):
    print(*ln)
