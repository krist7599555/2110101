# 04_P1
print(sum(1 for i in input() if i.isupper()))

# 04_P2
from functools import reduce
print(*reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), ((1, 0) if i in 'aeiouAEIOU' else (0, 1) for i in input() if i.isalpha()), (0, 0)))

# 04_P3
a, b = input().split()
print(a.title(), sum(ord(i) - ord('0') for i in b if i.isdigit()))

# 04_P4
m, d, y = map(int, input().split('/'))
print(format(d, '02d'), 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()[m-1].upper(), y)

# 04_P5
inp = input().strip()
print(inp, sum(map(int, inp)) & 1, sep = '')

# 04_P6
inp = input().strip()
print(inp, sum(map(int, inp)) & 1, sep = '')

# 04_P7
print(*sorted(set('0123456789') - set(input()) or ['No missing digits']))

# 04_P8
inp = list(input().lower())
print('yes' if sorted(inp) == inp else 'no')

# 04_P9
inp, a, b = tuple(input().strip() for i in range(3))
print(*({a:b,b:a}[c] if c in [a,b] else c for c in inp), sep='')

# 04_P10
inp, a, b = tuple(input().strip() for _ in range(3))
dic = dict([*zip(a, b), *zip(b,a)])
print(*(dic[c] if c in dic else c for c in inp), sep='')

# 04_P11
inp = input(); a, b = map(int, input().split())
print(inp[:a], inp[a:b+1][::-1], inp[b+1:], sep='')

# 04_P12
inp = input().strip().replace(' ', '').lower()
print(('no','yes')[inp == inp[::-1]])

# 04_P13
vow = [i for i, c in enumerate(input().lower()) if c in 'aeiou']
print(sum(1 for i, j in zip(vow, vow[1:]) if i + 1 != j) + 1 if vow else 0)

# 04_P14
print(eval(input()))

# 04_P15
from collections import defaultdict as dict
res = []
dic = dict(int)
for c in input():
	dic[c] += 1
	res.append(tuple([c, dic[c]]))
print(*(ch for ch, cnt in res if dic[ch] == 1 or cnt == 2), sep='')

# 04_P16
from functools import reduce
from itertools import chain
num = 'soon nueng song sam see ha hok jed pad kao'.split()
exp = '_ sip roey pun muen saen larn'.split()
spi = [('nueng-sip', 'sip'), ('song-sip', 'yee-sip'), ('sip-nueng', 'sip-ed')]

def to_thai(s):
	return chain(*((num[nm], exp[ex]) if ex else (num[nm],)
		for ex, nm in zip(range(len(s)-1,-1,-1), map(int, s)) if nm))
	
dig, flt, *_ = tuple([*input().replace(',', '').strip().split('.'), ''])
ans = []
if dig[0] == '-':
	ans.append('lop')
	dig = dig[1:]
if dig == '0':
	ans.append(num[0])
	dif = []
if len(dig) > 6:
	ans.extend(to_thai(dig[:-6]))
	ans.append(exp[6])
	dig = dig[-6:]
if dig:
	ans.extend(to_thai(dig))
if flt:
	ans.append('jood')
	ans.extend(map(lambda i: num[int(i)], flt))
print(reduce(lambda s, tp: s.replace(*tp), spi, '-'.join(ans)))

# 04_P17
from functools import reduce
num = dict(zip('soon nueng song sam see ha hok jed pad kao'.split(), range(12)))
exp = dict(zip('_ sip roey pun muen saen larn'.split(), range(7)))
spi = [('yee-sip', 'song-sip'), ('sip-ed', 'sip-nueng')]
	
dig, flt, *_ = tuple([*input().strip().split('jood'), ''])
ans, tmp, neg = 0, 0, False
dig = reduce(lambda s, tp: s.replace(*tp), spi, dig).split('-')
for s in dig:
	if not s: continue
	if s == 'lop': neg = True
	elif s in num:
		ans += tmp
		tmp = num[s]
	elif s in exp:
		if s == 'larn':
			if ans < 1e6:
				ans = (ans + tmp) * 10 ** exp[s]
				tmp = 0
			else:
				tmp *= 10 ** exp[s]
		elif s == 'sip':
			if 0 < tmp < 10:
				tmp *= 10
			else:
				ans += tmp
				tmp = 10
		else:
			tmp *= 10 ** exp[s]
	else: assert False
ans += tmp
print(format(-ans if neg else ans, ',d'), end='')
if flt:
	print('.', *[num[i] for i in flt.split('-') if i], sep='')
  
# 04_P18
from itertools import takewhile
from operator  import itemgetter as itemg
inp = list(input().strip() for _ in range(int(input())))
get_ans = lambda: ''.join(map(itemg(0), takewhile(lambda *tp: len(set(*tp)) <= 1, zip(*inp))))
print(get_ans() or 'NO COMMON PREFIX')
inp = map(itemg(slice(None,None,-1)), inp)
print(get_ans()[::-1] or 'NO COMMON SUFFIX')

# 04_P19
print(' '.join(sorted(set(input().strip()) & set(input().strip()), key=str.swapcase)) or 'NONE')

# 04_P20
x, y = 0, 0
for ch in input().strip():
	x, y = {
		'R': (x + 1, y),
		'U': (x, y + 1),
		'L': (max(x - 1, 0), y),
		'D': (x, max(y - 1, 0))
	}[ch];
print('({},{})'.format(x, y))

# 04_P21
a = input().strip(); b = input().strip(); ia = iter(a); ib = iter(b)
print(['NONE', 'SUBSEQUENCE', 'SUBSTRING'][(a in b) + all(any(ca == cb for cb in ib) for ca in ia)])
