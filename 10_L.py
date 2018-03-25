# 10_L1
print('CE AB H J DHJMN'.split()[int(input()) - 1])

# 10_L2
import functools
@functools.lru_cache()
def x(n):   return 3 * x(n-1) * (1-x(n-1)) if n else 0.01                           # Logistic Map
def M(n):   return M(n-1) + sum(M(k) * M(n-2-k) for k in range(n-1)) if n>1 else 1  # Motzkin number
def S(n):   return ((6*n-9) * S(n-1) - (n-3) * S(n-2)) / n if n >= 3 else 1         # Schroder-Hipparchus number
def d(n):   return n * d(n-1) + pow(-1, n) if n else 1                              # Number of Derangements
def D(m,n): return D(m,n-1) + D(m-1,n) + D(m-1,n-1) if n and m else 1               # Delannoy number
exec(input().strip())

# 10_L3
def dhanoi(n, l, m, r):
	__move = lambda *args: print('{}{} : {} -> {}'.format(*args))
	if n == 0 : return
	dhanoi(n-1, l, m, r)
	__move(n, 'W', l, m)
	__move(n, 'B', l, m)
	dhanoi(n-1, r, m, l)
	__move(n, 'B', m, r)
	__move(n, 'W', m, r)
	dhanoi(n-1, l, m, r)
exec(input().strip())

# 10_L4
def copylist(x):
    try:    return list(map(copylist, x))
    except: return x
exec(input().strip())
