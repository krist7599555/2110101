# 10_V1
print('chmcgqahkceg'[int(input()) - 1])

# 10_V2
def gcd(x,y): return gcd(y, x % y) if y else x      	                # Greatest Common Divisor
def A(m,n): return A(m-1, A(m,n-1)if n else 1) if m else n + 1 		# Ackermann Number
def J(n,k): return (J(n-1, k) + k) % n if n > 1 else 0 			# Josephus Problem
def C(n): return sum(C(i) * C(n-i-1)for i in range(n)) if n else 1 	# Catalan Number
def h(n): return 2 * h(n-1) +1 if n else 0  				# Tower of Hanoi
def F(n): return n - M(F(n-1)) if n else 1 				# Female sequence
def M(n): return n - F(M(n-1)) if n else 0 				# Male sequence
def f(n): return n if n<=1 else f((n+1)//2)**2 + f(n//2)**2 if n & 1 \
			else (2 * f(n//2-1) + f(n//2)) * f(n//2)	# Fibonacci Number
exec(input().strip())

# 10_V3
from random import randrange as rand
def qsort(ls):
  if not ls: return []
  pivot = ls.pop(rand(len(ls)))
  return qsort([i for i in ls if i < pivot]) \
    + [pivot] + qsort([i for i in ls if i >= pivot]) 
print(*qsort(list(map(int, input().split()))))

# 10_V4
def sumls(x):
    return sum(map(sumls, x)) if isinstance(x, list) else x
print(sumls(eval(input().strip())))
