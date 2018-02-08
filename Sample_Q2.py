# Sample_Q2_1
nm_pf = 0
for _ in range(int(input())):
    n = int(input())
    ls = [d for d in range(1, n // 2 + 1) if not n % d]
    if n == sum(ls):
        nm_pf += 1
        print(n, 'is perfect')
        print(*ls, '', sep=',')
    else:
        print(n, 'is not perfect')
print(nm_pf)

# Sample_Q2_2
base = int(input())
for i in range(*[int(i,base) for i in input().split()]):
    ls = ''
    while i:
        ls += str(i % base)
        i //= base
    print(ls[::-1] or '0')

# Sample_Q2_3
dc = dict(zip('A234567890JQK', range(13)))
def ok(s):
    l = list(map(dc.get, s.strip()))
    return 'NY'[l == sorted(l)]
print(list(map(ok, open('cards.txt')))[int(input()) - 1])

# Sample_Q2_4
ans = ''
s = input().strip()
for i in range(len(s)):
    for j in range(i + len(ans), len(s) + 1):
        k = s[slice(i, j)]
        if k == k[::-1]:
            ans = k if len(k) > len(ans) else min(ans, k)
print(ans)
