def solve_1(n):
    while n > 1:
        if n & 1:
            print(n)
            n = n * 3 + 1
        print(n)
        n //= 2
    print('1' if n else '0!')

def solve_2(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if 'a' <= s[j] < s[i] <= 'z':
                s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
    print(s)

def solve_3(n, k):
    if 0 <= k <= n >= 1:
        s = '01'
        for i in range(1, n):
            o = ''
            for j in range(0, len(s), i):
                o += s[j: j+i] + '0'
                o += s[j: j+i] + '1'
            s = o
        for i in range(0, len(s), n):
            o = s[i: i+n]
            if o.count('1') == k:
                print(o)
    else:
        print('empty')
        
solve_1(0)
solve_1(1)
solve_1(2)
solve_1(3)
solve_1(4)
solve_1(7)
solve_1(19)
solve_1(10)
solve_2('bca')
solve_2('bcaBAC')
solve_2('Abb12BcaC123')
solve_2('')
solve_2('1c2a34c56c78c9b')
solve_2('AaBbbCCCcDef12435ADVBFadsfbBRFRWb')
solve_2('A aBb b C CC!ncD **e)f12m435ADVB# @@Fad!! sf()(bBRFRWb')
solve_3(0, 0)
solve_3(0, 7)
solve_3(1, 7)
solve_3(1, 1)
solve_3(4, 2)
solve_3(4, 4)
solve_3(6, 3)
solve_3(6, 2)
solve_3(6, 9)
