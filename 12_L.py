# 12_L1
print('cddcc'[int(input()) - 1])

# 12_L2
class rint :
	def __init__(self, s): self.s = str(s)
	def __str__(self): return str(self.s)
	def __int__(self): return int(self.s[::-1])
	def __lt__ (lhs, rhs): return int(rhs.s) < int(lhs.s)
	def __add__(lhs, rhs): return rint(str(int(lhs)+int(rhs))[::-1])
t, a, b = input().split()
a, b = map(rint, [a, b])
print(*{
	'1': [a < b],
	'2': [int(a),int(b)],
	'3': [str(a),str(b)],
	'4': [int(a + b)],
	'5': [str(a + b)]
}[t])

# 12_L3
import numpy as np
class Complex:
    def get(s): return s.re, s.im
    def __init__(s, re, im): s.re, s.im = re, im
    def __str__(s):
        a, b = s.get()
        ls = [str(a), ['','+','-'][int(np.sign(b))], str(abs(b)), 'i'] 
        if ls[2] == '1': ls.pop(2)
        if not b: return ''.join(ls[:1])
        if not a: return ''.join(ls[1:]).lstrip('+')
        return ''.join(ls) if a and b else '0'
    def __add__(lh, rh):
        return Complex(lh.re + rh.re, lh.im + rh.im)
    def __mul__(lh, rh):
        a, b, c, d = *lh.get(), *rh.get()
        return Complex(a * c - b * d, a * d + b * c)
    def __truediv__(lh, rh):
        a, b, c, d = *lh.get(), *rh.get(); e = c ** 2 + d ** 2
        return Complex((a*c + b*d) / e, (-a*d + b*c) / e) if e else None 
t, a, b, c, d = map(int, input().split())
c1, c2 = map(Complex, [a, c], [b, d])
print([c1, c2, c1+c2, c1*c2, c1/c2][t-1])

# 12_L4
class piggybank:
	def __init__(self):
		self.coin = dict()
		self.limt = 100
	def add(self, v, n):
		if self.limt < n: return False
		v = float(v)
		self.limt -= n
		self.coin[v] = self.coin.get(v, 0) + n
		return True
	def __float__(self): 
		return __import__('math').fsum(v * n for v, n in self.coin.items())
	def __str__(self): 
		return '{' + ', '.join('{}:{}'.format(*tp) for tp in sorted(self.coin.items())) + '}'
p1, p2 = piggybank(), piggybank()
exec(input())
exec(input())
