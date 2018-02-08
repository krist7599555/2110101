# 59_2_Q1_2_p
d, m, y = map(int, input().split())
k = y - 543 + 4000000
assert k > 0
f = (28, 29)[bool(not k % 400 or (not k % 4 and k % 100))]
t = [None, 31, f, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d += 15
if d > t[m]:
    d -= t[m]
    m += 1
if m > 12:
    m -= 12
    y += 1
print(d, m, y, sep = '/')

# 59_2_Q1_3_p
a, b, c = map(float, input().split())
fmt = '{:.2f}'.format
if not a:
    if not b:
        print(('No roots exists',
               'Roots are any numbers')[bool(not c)])
    else:
        print(fmt(-c / b))
else:
    cpx = pow(b, 2) - 4 * a * c
    if   cpx <  0:  print('Roots are complex numbers')
    elif cpx == 0:  print(fmt(-b / (2 * a)))
    else:
        cpx = pow(cpx, .5)
        print(*map(fmt, sorted([
            (-b + cpx) / (2 * a),
            (-b - cpx) / (2 * a)
        ])))

# 59_2_Q1_4_p
from math import sin, pi
def biorythm(t):
	return [sin(2 * pi * t / x) for x in [23, 28, 33]]
def day(d, m, y):
	k = y - 543 + 4000
	f = 29 if not k % 400 or (not k % 4 and k % 100) else 28
	mnt = [0, 31, f, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	return d + sum(mnt[:m]), sum(mnt)
d1, m1, y1, d2, m2, y2 = map(int, input().split())
x1, a1 = day(d1, m1, y1)
x2, a2 = day(d2, m2, y2)
md = sum([a1 - x1, 365 * (y2 - y1 - 1), x2])
print(md, *map('{:.2f}'.format, biorythm(md)))
