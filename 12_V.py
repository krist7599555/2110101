# 12_V1
print('cdcdd'[int(input()) - 1])

# 12_V2
import math
class Circle:
    def __init__(self, i, x, y, r):
        self.i, self.x, self.y, self.r = i, x, y, r
    def touch(lhs, rhs):
        return math.hypot(lhs.x - rhs.x, lhs.y - rhs.y) < lhs.r + rhs.r
n = int(input())
cyc = [Circle(*map(int, input().split())) for _ in range(n)]
print(*[c.i for c in cyc if all(not c.touch(t) for t in cyc if c is not t)] or ['Not Found'])


# 12_V3
import math
from collections import namedtuple

class Point(namedtuple('Point', ['x', 'y'])):
	def distance(p1, p2):
		return math.hypot(p1.x - p2.x, p1.y - p2.y)
	
class Line:
	def __init__(self, x1, y1, x2, y2):
		self.p1 = Point(x1, y1)
		self.p2 = Point(x2, y2)
		
	def __contains__(cls, rhs):
		if isinstance(rhs, Point):
			x1, y1, x2, y2, px, py = *cls.p1, *cls.p2, *rhs
			if not (min(y1, y2) <= py <= max(y1, y2)): return False
			return abs((y1-py)*(x2-x1)-(y2-y1)*(x1-px)) < 1e-5 if x1 != x2 else px == x1
		raise NotImplemented
		
class Circle(Point):
	def __new__(cls, idx, x, y, r):
		cls.idx, cls.r = idx, r
		return Point.__new__(cls, x, y)
		
	def line_intersection(circ, line):
		x1, y1, x2, y2, xc, yc, rc = *line.p1, *line.p2, *circ, circ.r
		if x1 != x2:
			M = (y2-y1)/(x2-x1) # line: y = Mx+B
			B = y1 - M * x1
			a = M**2+1
			b = -2*xc + 2*M*(B-yc)
			c = pow(xc,2) + pow(B-yc,2) - pow(rc,2)
			z = b**2 - 4*a*c # discriminant
			if z > 0:
				ans1 = (-b + math.sqrt(z))/2/a
				ans2 = (-b - math.sqrt(z))/2/a
				return [Point(ans1, M*ans1+B), Point(ans2, M*ans2+B)]
			return   [Point(-b/2/a, M*(-b/2/a)+B)] if z is 0 else[]
		else:
			if rc**2 > (x1-xc)**2:
				rr = math.sqrt(rc**2 - (x1-xc)**2)
				return [Point(x1, rr+yc),Point(x2, rr-yc)]
			return   [Point(x1, yc)] if rc**2 == (x1-xc)**2 else []
			
	def __contains__(circ, rhs):
		if isinstance(rhs, Point):
			return Point.distance(circ, rhs) <= circ.r
		if isinstance(rhs, Line):
			if rhs.p1 in circ or rhs.p2 in circ: return True
			return any(p in line for p in circ.line_intersection(line))
		raise NotImplemented

if __name__ == '__main__':
	n = int(input().strip())
	line = Line(*map(int, input().split()))
	ans = []
	for i in range(n):
		circle = Circle(*map(int, input().split()))
		if line in circle:
			ans.append(str(circle.idx))
	print(' '.join(map(str, ans)) or 'Not Found')
	
	
# 12_V4	
import math
import itertools
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

class Cycle(Point):
	def __new__ (self, x, y, *_): return super(Cycle, self).__new__(self, x, y)
	def __init__(self, x, y, r=0, s=0): self.r, self.s = r, s
	def distance (lhs, rhs): return math.hypot(lhs.x - rhs.x, lhs.y - rhs.y)
	def intersect(lhs, rhs): return lhs.distance(rhs) <= lhs.r + rhs.r
	def area (self): return math.pi * self.r ** 2
	def scale(self): return self.area() * self.s
		
n = int(input())
p = Cycle(*map(float, input().split()))
grp = []
for _ in range(n):
	tmp = list(map(float, input().split()))
	nw = Cycle(*tmp)
	inc, exc = [[nw]], []
	for ls in grp:
		[exc, inc][any(map(nw.intersect, ls))].append(ls)
	grp = exc + [list(itertools.chain(*inc))]
for ls in grp:
	if any(map(p.intersect, ls)):
		print(sum(map(Cycle.scale, ls)) / sum(map(Cycle.area, ls)))
		break
else:
	print(1.0)
