# 09_L1
print('daaea'[int(input()) - 1])

# 09_L2
from functools import partial
def knows(R, x, y): return y in R[x]
def is_celeb(R, x):
	return all(x in t for s, t in R.items() if s != x) \
	   and not any(1 for t in R[x] if t != x)
def find_celeb(R):
	return next(filter(partial(is_celeb, R), R), None)
def read_relations() :
	R = __import__('collections').defaultdict(set)
	while True:
		try:
			a, b = input().split()
			R[a].add(b); R[b]
		except: return R
def main():
	print(find_celeb(read_relations()) or 'Not Found')
exec(input().strip())

# 09_L3
remove_comma  = lambda t: t.replace(',' , '')
extract_sign  = lambda t: ('lop-', t[1:]) if t[0] == '-' else ('', t)
split_by_point   = lambda t: (t.split('.') + [''])[:2]
split_by_million = lambda t: ('', t) if len(t) <= 6 else (t[:-6], t[-6:])
combine  = lambda a, b: ((a + '-larn-' if a else '') + b).strip('-') or'soon'
dig2text = lambda t: 'soon nueng song sam see ha hok jed pad kao'.split()[t]
pos2text = lambda t:'_ sip roey pun muen saen larn'.split()[t].strip('_')
jood2text= lambda t: '-jood'+''.join('-' + dig2text(int(d)) for d in t) if t else ''
def number_to_text(t):
	s, t = extract_sign(t)
	t, c = split_by_point(t)
	a, b = split_by_million(remove_comma(t))
	def _num2text(x):
		rs = ''
		for i, c in enumerate(x[::-1]):
			if c != '0':
			  rs = '-'.join([dig2text(int(c)), pos2text(i), rs]).strip('-')
		return rs .replace('song-sip', 'yee-sip')\
				      .replace('nueng-sip', 'sip')\
				      .replace('sip-nueng', 'sip-ed')
	return s + combine(*map(_num2text, [a, b])) + jood2text(c)
def main():
	print(number_to_text(input().strip()))
exec(input().strip())

# 09_L4
def flatten(t):       return list(v for ls in t for v in ls if v)
def inversions(x):    return sum (1 for i, vr in enumerate(x) for vl in x[:i] if vr < vl)
def row_number(t, e): return next(i for i, ls in enumerate(t) if e in ls)
def solvable(t):
    inv = inversions(flatten(t))
    return bool([(inv ^ row_number(t, 0)) & 1, ~inv & 1][len(t)&1])
exec(input())
