# 09_P1
def is_prime (n): return n > 1 and all(n % i for i in range(2, int(n ** .5) + 1))
def function1( ): print(45)
def function2(n): print(is_prime(int(n)))
def function3(n): print(*filter(is_prime, range(1, int(n))), sep='\n')
def function4(x,y): t = x.count(y); print([t, x.replace(y, '')])
from sys import stdin
globals()[next(stdin).strip()](*next(stdin, '').split())

# 09_P2
import math
def next_even_odd(i):
    return (i+1, i) if i & 1 else (i, i+1)
while True:
    x = math.ceil(float(input()))
    if x < 0: break
    print(next_even_odd(x))
    
# 09_P3
print(*map(' '.join, sorted([input().split() for _ in range(int(input()))], 
  key=lambda t:[-float(t[1]), t[0]])), sep='\n')
  
# 09_P4
import numpy as np
print(int(round(np.linalg.det(np.matrix([input().strip().split() for _ in range(4)], dtype=np.int)))))

# 09_P5
def roman_to_int(s):
    table = [['M',1000],['CM',-200],['D',500],['CD',-200],['C',100],['XC',-20],\
             ['L',50],['XL',-20],['X',10],['IX',-2],['V',5],['IV',-2],['I',1]]
    return sum(s.count(i) * j for i, j in table)
print(*sorted([input() for _ in range(int(input()))], key=roman_to_int), sep='\n')

# 09_P6
from collections import defaultdict
def read_data():
    dic = defaultdict(set)
    for _ in range(int(input())):
        pdf, *kwd = input().split()
        for w in kwd:
            dic[w].add(pdf)
    return dic
def search(dic, cmd, kwd):
    ls = [dic[w] for w in kwd]
    return {
      'or' : set.union(*ls),
      'and': set.intersection(*ls)
    }.get(cmd, [])
doc, tok = read_data(), input().split()
print(sorted(search(doc, tok[0], tok[1:])))

# 09_P7
f, f_inv = lambda x: x * (x+2) + 3, lambda y: int(pow(y-2, .5)) - 1
print(eval(input().strip()))

# 09_P8
from itertools import product
def is_set(*args):
	return all(len(set(tp)) != 2 for tp in zip(*args))
cards = [input().strip().split() for _ in range(12)]
for i, j, k in product(range(12), repeat=3):
	if i < j < k and is_set(cards[i],cards[j],cards[k]):
		print(i, j, k)
		
# 09_P9		
from itertools import count
def isSevenUp(x):   return not x % 7 or '7' in str(x)
def nextSevenUp(x): return next(filter(isSevenUp, count(x+1, 1)))
def prevSevenUp(x): return next(filter(isSevenUp, count(x-1,-1)))
f, x = input().split()
print(globals()[f](int(x)))

# 09_P10
from math import hypot
def perimeter(p):
	return sum(hypot(x1-x2, y1-y2) for (x1,y1),(x2,y2) in zip(p[-1:]+p, p))
print(perimeter(list(map(eval, input().split()))))

# 09_P11
import numpy as np
def zscore(ls):
    std = np.std(ls)
    mean = np.mean(ls)
    return (ls - mean) / std
for i in zscore(np.array(input().split(), dtype=np.float)):
    print(i)
    
# 09_P12    
from itertools import product
def eat(a, b):
	s = set([abs(a[0] - b[0]), abs(a[1] - b[1])])
	return len(s) == 1 or 0 in s
def all_eat(ls):
	return [(i, j) for i, j in product(range(len(ls)), repeat=2) 
	  if i < j and eat(ls[i], ls[j])]
print(eval(input().strip()))

# 09_P13
def row_number(t, e): return next(i for i, l in enumerate(t) if e in l)
def flatten(t):       return [v for l in t for v in l if v != 0]
def inversions(x):    return sum(1 for r in range(len(x))for l in range(r) if x[l] > x[r])
def solvable(t): 
	siz, inv = len(t) & 1, inversions(flatten(t)) & 1
	return (siz and not inv) or (not siz and (inv != row_number(t, 0) % 2))
exec(input().strip())
