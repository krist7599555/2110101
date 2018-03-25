# 12_P1
import math
class ComplexNum:
    def __init__(self,re,im): self.re, self.im = re, im
    def __str__(self): return '{}{:+d}i'.format(self.re, self.im)
    def __abs__(self): return math.hypot(self.re, self.im)
    def __add__(lh,rh):return ComplexNum(lh.re+rh.re, lh.im+rh.im)
    def conj(self):    return ComplexNum(self.re, -self.im)
a, b, c, d = map(int, input().split())
x1, x2 = map(ComplexNum, [a, c], [b, d])
print(x1, x1.conj(), round(abs(x1), 2))
print(x2, x2.conj(), round(abs(x2), 2))
print(x1 + x2)

# 12_P2
import math
class Fraction:
    def __init__(self, a, b):
        g = math.gcd(a, b)
        self.num = a // g
        self.dnm = b // g
    def __str__(self): return '{}/{}'.format(self.num, self.dnm)
    def __add__(l, r): return Fraction(l.num * r.dnm + l.dnm * r.num, l.dnm * r.dnm)
    def __mul__(l, r): return Fraction(l.num * r.num, l.dnm * r.dnm)
a, b, c, d = map(int, input().split())
f1 = Fraction(a, b)
f2 = Fraction(c, d)
print(f1 + f2)
print(f1 * f2)

# 12_P3
class Card:
    def __init__(t, val, suit): t.v, t.s = val, suit
    def __str__ (t): return '({} {})'.format(t.v, t.s)
    def __int__ (t): return min('A234567891JQK'.index(t.v[0]) + 1, 10)
    def sum(lh, rh): return (int(lh) + int(rh)) % 10
    def __lt__(lh, rh):
        f = '34567891JQKA2'.index
        return [f(lh.v[0]), lh.s] < [f(rh.v[0]), rh.s]
c = [Card(*input().split()) for _ in range(int(input()))]
print(*map(int, c), sep='\n')
print("----------")
print(*map(Card.sum, c, c[1:]), sep='\n')
print("----------")
print(*sorted(c), sep='\n')

# 12_P4
from itertools import product
class Card:
	card = '3 4 5 6 7 8 9 10 J Q K A 2'.split()
	suit = 'club diamond heart spade'.split()
	ordr = list(product(card, suit))
	def __init__(obj, c, s): obj.x = Card.ordr.index((c, s))
	def __str__ (obj): return '({} {})'.format(*Card.ordr[obj.x])
	def next1(obj): return Card(*Card.ordr[(obj.x+1) % len(Card.ordr)])
	def next2(obj): obj.x = obj.next1().x
cards = [Card(*input().split()) for _ in range(int(input()))]
print(*map(Card.next1, card

# 12_P5
from collections import namedtuple

class Point(namedtuple('Point', ['x', 'y'])):
	def __str__(cls):
		return '({},{})'.format(*cls)
		
class Rect(namedtuple('Rect', ['tl', 'br'])):
	def area(cls):
		return (cls.tl.x - cls.br.x) \
			 * (cls.tl.y - cls.br.y)
	def __contains__(cls, poi):
		return cls.tl.x <= poi.x <= cls.br.x\
		   and cls.tl.y <= poi.y <= cls.br.y

x1, y1, x2, y2 = map(int, input().split())
rect = Rect(Point(x1, y1), Point(x2, y2))
print(rect.area())
for i in range(int(input())):
	print(Point(*map(int, input().split())) in rect)
	
	
# 12_P6
from collections import namedtuple

class Point(namedtuple('Point', ['x', 'y'])):
	def __str__(cls):
		return '({},{})'.format(*cls)

class Rect(namedtuple('Rect', ['tl', 'br'])):
	def area(cls):
		return (cls.tl.x - cls.br.x) \
			 * (cls.tl.y - cls.br.y)
	def __contains__(cls, poi):
		return cls.tl.x <= poi.x <= cls.br.x\
		   and cls.tl.y <= poi.y <= cls.br.y
	def __str__(cls):
		return '{}-{}'.format(*cls)
		
rect = []
for _ in range(int(input())):
	x1, y1, x2, y2 = map(int, input().split())
	rect.append(Rect(Point(x1,y1), Point(x2,y2)))
print(*sorted(rect, key=Rect.area), sep='\n')


# 12_P7
class piggybank:
    def __init__(s): s.d = dict(zip([1,2,5,10], [0,0,0,0]))
    def add1 (s, n): s.d[1 ] += n
    def add2 (s, n): s.d[2 ] += n
    def add5 (s, n): s.d[5 ] += n
    def add10(s, n): s.d[10] += n
    def __int__(s): return sum(i * j for i, j in s.d.items())
    def __str__(s): return '{{1:{}, 2:{}, 5:{}, 10:{}}}'.format(*map(s.d.get, [1,2,5,10]))
    def __lt__(lhs, rhs): return int(lhs) < int(rhs)
p1 = piggybank()
p2 = piggybank()
exec(input())
exec(input())

# 12_P8
from itertools import starmap
from collections import defaultdict
class piggybank:
	def __init__(cls):
		cls.c = 100     
		cls.d = defaultdict(int)
	def add(cls, v, n):
		if n <= cls.c:
			cls.c -= n
			cls.d[float(v)] += n
			return True
		return False
		
# 12_P9
class rational:
	def __init__(s, n, d): s.n, s.d = n, d
	def __str__  (s):  return '{}/{}'.format(s.n, s.d)
	def __float__(s):  return s.n / s.d
	def __neg__  (s):  return rational(-s.n, d)
	def __lt__ (l, r): return float(lh) < float(rh)
	def __mul__(l, r): return rational(l.n * r.n, l.d * r.d)
	def __add__(l, r): return rational(l.n * r.d + l.d * r.n, l.d * r.d)
	def __sub__(l, r): return rational(l.n * r.d - l.d * r.n, l.d * r.d)
	def __truediv__(l, r): return rational(l.n * r.d, l.d * r.n)
print(float(eval('rational({1}, {2}) {0} rational({3}, {4})'.format(*input().split()))))	

# 12_P10
import math
class rational:
	def __init__(s, n, d): g = math.gcd(n,d); s.n, s.d = n // g, d // g
	def __str__  (s):  return '{}{}/{}'.format(('','-')[float(s) < 0], *map(abs,[s.n,s.d]))
	def __float__(s):  return s.n / s.d
	def __neg__  (s):  return rational(-s.n, d)
	def __lt__ (l, r): return float(lh) < float(rh)
	def __mul__(l, r): return rational(l.n * r.n, l.d * r.d)
	def __add__(l, r): return rational(l.n * r.d + l.d * r.n, l.d * r.d)
	def __sub__(l, r): return rational(l.n * r.d - l.d * r.n, l.d * r.d)
	def __truediv__(l, r): return rational(l.n * r.d, l.d * r.n)
print(eval('rational({1}, {2}) {0} rational({3}, {4})'.format(*input().split())))

# 12_P11
class roman:
	c  = 'I IV V IX X XL L XC C CD D CM M'.split()
	v1 = [1, -2, 5, -2, 10, -20, 50, -20, 100, -200, 500, -200, 1000]
	v2 = [1,  4, 5,  9, 10,  40, 50,  90, 100,  400, 500,  900, 1000]
	def __init__(cls, v): 
		if isinstance(v, str):
			    cls.s, cls.i = v, roman.roman2int(v)
		else: cls.s, cls.i = roman.int2roman(v), v
	def __str__(cls): return cls.s
	def __int__(cls): return cls.i
	def __lt__ (lhs, rhs): return lhs.i < rhs.i
	def __add__(lhs, rhs): return roman(lhs.i + rhs.i)
	def roman2int(s): 
		return sum(s.count(c) * v for c, v in zip(roman.c, roman.v1))
	def int2roman(i):
		sm = ''
		for c, v in zip(roman.c[::-1], roman.v2[::-1]):
			while i >= v: 
			  i -= v; sm += c
		return sm
	
t, a, b = input().split()
a, b = map(roman, [a, b])
print(*{
  '1': [bool(a < b)],
  '2': [int(a), int(b)],
  '3': [str(a), str(b)],
  '4': [int(a + b)],
  '5': [str(a + b)]
}[t])
