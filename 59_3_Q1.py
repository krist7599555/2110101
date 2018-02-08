# 59_3_Q1_2_p
a, b, c, d = map(int, input().split())
if a > b:
    a, b = b, a
    if d >= a:
        if c > d:
            c -= a
    else:
        c += a
    b = a + c + d
else:
    if c > a >= b:
        d += a
    if d > c:
        if ~d & 1:
            b += 2
    else:
        b *= 2
print(a, b, c, d)

# 59_3_Q1_3_p
from math import sqrt, tan, radians
ls = {
    3: sqrt(3) / 4,
    4: 1,
    5: .25 * sqrt(5 * (5 + sqrt(20))),
    6: sqrt(27) / 2,
    7: 7 / (4 * tan(radians(180)/7))
}
f = float(input())
n = int(input())
print(round(ls[n] * pow(f, 2), 3) if n in ls else 'N/A')

# 59_3_Q1_4_p
def solve(d, m, y, n):
    k = y - 543 + 4000
    f = 29 if not k % 400 or (not k % 4 and k % 100) else 28
    mth = [None, 31, f, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dic = dict(zip('EQNF', [1, 3, 7, 14]))

    if   y < 2558:              print('Invalid year')
    elif m < 1 or m > 12:       print('Invalid month')
    elif d < 1 or d > mth[m]:   print('Invalid date')
    elif n not in dic:          print('Invalid delivery type')
    else:
        d += dic[n]
        if d > mth[m]:
            d -= mth[m]
            m += 1
        if m > 12:
            m -= 12
            y += 1
        print('delivered on {}/{}/{}'.format(d, m, y))
while True:
    d, m, y = map(int, input().split())
    n = input().strip()
    solve(d, m, y, n)
    break
