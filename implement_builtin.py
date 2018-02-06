def _get_mnmx(*con, default = None, key = lambda x: x, mnmx):
	ls = list(con)
	if len(ls) == 1:
		ls = ls[0]
	it = iter(ls)
	rs = default or next(it)
	for vl in it:
		if mnmx(key(vl), key(rs)):
			rs = vl
	return rs
	
def min_(*args, **kwarg):
	return _get_mnmx(*args, **kwarg, mnmx = lambda a, b: a < b)
	
def max_(*args, **kwarg):
	return _get_mnmx(*args, **kwarg, mnmx = lambda a, b: a > b)

def range_(s, t = None, d = 1):
	assert d != 0
	if t is None and d == 1:
		i = 0
		while i != max_(s, 0):
			yield i
			i += 1
	elif s < t and d > 0:
		while s < t:
			yield s
			s += d
	elif s > t and d < 0:
		while s > t:
			yield s
			s += d
				
	
def fac_(nm):
	rs = 1
	for i in range_(1, nm + 1):
		rs *= i
	return rs
	
def zip_(*con):
	con = [iter(e) for e in con]
	while True:
		ls = []
		for it in con:
			ls.append(next(it))
		yield tuple(ls)
		
def map_(func, *con):
	for vl in zip_(*con):
		yield func(*vl)

def sum_(con, init = 0):
	for vl in con:
		init += vl
	return init
	
def bin_(nm):
	if not nm:
		return '0b0'
	sg = ''
	if nm < 0:
		nm = -nm
		sg = '-'
	s = []
	while nm:
		s.append(nm & 1)
		nm >>= 1
	return sg + '0b' + ''.join(map_(str, s[::-1]))
	
def sorted_(con, *_, key=lambda x:x, reverse=False):
	assert not _
	ls = list(con)
	ln = len(ls) // 2
	if not ln:
		return ls
	a = sorted_(ls[:ln], key=key, reverse=reverse)
	b = sorted_(ls[ln:], key=key, reverse=reverse)
	i, j = 0, 0
	rs = list()
	while i != len(a) and j != len(b):
		if (key(a[i]) < key(b[j])) ^ reverse:
			rs.append(a[i]); i += 1
		else:
			rs.append(b[j]); j += 1
	return rs + a[i:] + b[j:]

def all_(it):
	for i in it:
		if not i:
			return False
	return True
	
def any_(it):
	for i in it:
		if i:
			return True
	return False
	
def filter_(func, con):
	for vl in con:
		if func(vl):
			yield vl

def reversed_(con):
	return list(con)[::-1]

def reduce_(func, con, init = None):
	it = iter(con)
	rs = init or next(it)
	for vl in it:
		rs = func(rs, vl)
	return rs
	
def count_(s, t = 1):
	while True:
		yield s
		s += t

def cycle_(ls):
	ls = list(ls)
	while True:
		for i in ls:
			yield i

def repeat_(item, loop = -1):
	while loop:
		yield item
		loop -= 1

def chain_(*it):
	for vl in it:
		for i in vl:
			yield i

def product_(*args, repeat=1):
	ls = list(map_(tuple, args)) * repeat
	rs = [[]]
	for vl in ls:
		rs = [i + [j] for i in rs for j in vl]
	for vl in rs:
		yield tuple(vl)

	
