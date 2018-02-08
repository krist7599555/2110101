# 59_2_Q2_2_p
def solve(i):
    if not i: return '0 = 0'
    sg = i < 0
    s = str(abs(i))
    l = ['{}*1{}'.format(i, '0'*j) for i, j in zip(s[::-1], range(len(s))) if i != '0']
    s = ' + '.join(reversed(l))
    if sg:
        s = '-' + s.replace('+', '-')
    return '{} = {}'.format(i, s)
print(solve(int(input())))

# 59_2_Q2_3_p
from string import *
def nxt(c, k):
    for ls in [digits, ascii_lowercase, ascii_uppercase]:
        if c in ls:
            return ls[(ord(c) - ord(ls[0]) + k) % len(ls)]
    return c
def solve(s):
    out, cnt, offset, c_num = '', 0, -1, -1
    for c in s:
        if  offset == -1: offset = int(c)
        elif c_num == -1: c_num  = int(c)
        else:
            cnt += 1
            out += nxt(c, offset)
            if cnt == c_num:
                cnt, offset, c_num = 0, -1, -1
    return out
print(solve(input().strip()))


# 59_2_Q2_4_p
from collections import deque
f = open(input().strip())
n = int(input())
dq = deque(maxlen = n + 1)
for l in f:
    s = l.strip().split(';', 1)[1]
    dq.append(s)
    if ';Failure' in s:
        print(*dq, sep='\n')
        break
else:
    print('Not Found')
