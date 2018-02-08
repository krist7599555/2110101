# Sample_Q1_1
from math import pi, acos, sqrt
r, g, b = [float(input()) for _ in range(3)]
t = 2 * sqrt(pow(r - g, 2) + (r - b)*(g - b))
h = 2 * pi - acos((2 * r - g - b) / t)
i = (r + g + b) / 3
s = 1 - r / i
print(h, s, i, sep='\n')

# Sample_Q1_2
a, b, c = map(int, input().split())
d = b // a + c % a if a and (c % a or not b % a) else int(input())
if d < b:
    b *= 2
    a, c = c, a
    if b > a + c:
        d += b // 2
        c -= 1
if d < b and ~d & 1:
    a += b - d
    c += 1
elif d == b:
    a -= 1
elif d > a + c:
    b **= 2
else:
    d += b
print(a, b, c, d)

# Sample_Q1_3
from math import ceil
n = ceil(float(input()))
if not n:
    print('ERROR')
    __import__('sys').exit(0)
p = 0
l1 = [35, 5.5, 6.5, 7.5, 8, 9, 10.5]
l2 = [1, 9, 10, 20, 20, 20, float('inf')]
for c, l in zip(l1, l2):
    d = min(n, l)
    n -= d
    p += d * c
print(p if not n else 'ERROR')

# Sample_Q1_4
s, n = input().split()
n = int(n)
c = int(s[-n])
x = int(s[-n-1]) & 1 if c == 5 else c > 5
s = int(s[:-n] + '0' * n) + (pow(10, n) if x else 0)
print(s)
