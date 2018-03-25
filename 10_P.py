# 10_P1
def fac(n):
  return n * fac(n-1) if n else 1
print(fac(int(input())))

# 10_P2
def fib(n):
  return n if n <= 1 else fib(n-1) + fib(n-2)
print(fib(int(input())))

# 10_P3
def combi(n, k):
	return 1 if k in [0, n] else combi(n-1, k) + combi(n-1, k-1) if k <= n else 0
print(combi(*map(int, [input(), input()])))

# 10_P4
print(pow(*map(int, input().split())))

# 10_P5
def is_in(ls, vl):
	try:    return any(is_in(it, vl) for it in ls)
	except: return ls == vl
print(['Not Found', 'Found'][is_in(eva

# 10_P6
w = list(map(int, input().split()))
v = list(map(int, input().split()))
def f(t, i = 0):
    return max(f(t, i+1), v[i] + f(t-w[i], i+1) if t >= w[i] else 0) if i != len(w) else 0
print(f(int(input())))

# 10_P7
def max_sorted(ls, i=0, cur=1):
	if i + 1 == len(ls): return cur
	if ls[i] <= ls[i+1]: 
		  return max_sorted(ls, i+1, cur+1);
	else: return max(cur, max_sorted(ls, i + 1))
ls = list(map(int, input().split()))
print(max_sorted(ls))

# 10_P8
def gcd(a, b): return gcd(b % a, a) if a and b else a + b
print(gcd(*map(int, input().split())))

# 10_P9
n = input(); ls = list(map(int, input().split()))
print('true' if sorted(ls) in [ls, ls[::-1]] else 'false')

# 10_P10
def tiling(n, c = False):
    return 2 * tiling(n-1, False) + (tiling(n-1, True) if not c else 0) if n else 1
print(tiling(int(input())))

# 10_P11
import numpy as np
def show(mat):
	for i in range(9):
		m = list(mat[i,:])
		if not i % 3: print('+---+---+---+')
		print('|', *m[:3], '|', *m[3:6], '|', *m[6:], '|', sep='')
	print('+---+---+---+')	
def solve(mat):
	for i, j in zip(*np.where(mat == 0)):
		i_, j_ = i // 3 * 3, j // 3 * 3
		s = set(range(1, 10)) - set.union(*map(set, [
			mat[i,:], 
			mat[:,j], 
			mat[i_: i_+ 3, j_: j_+ 3].reshape(-1)
		]))
		for vl in s:
			mat[i, j] = vl
			tmp = solve(mat)
			if tmp is not None:
				return tmp
		else:
			mat[i, j] = 0
			return None
	else:
		return mat
show(solve(np.array(list(input().replace('.', '0').strip()), dtype=np.int).reshape(9, 9)))

# 10_P12
def recur(ls):
	if isinstance(ls, list):
		ans = []
		for vl in ls:
			ans.extend([recur(vl)] * 2)
		return ans
	else:
		return ls
print(recur(eval(input())))

# 10_P13
def recur(s, i=0, ls=[]):
	if i == len(s):
		yield ''.join(ls)
	else:
		if s[i].isupper():
			yield from recur(s, i+1)
		ls.append(s[i])
		yield from recur(s, i+1)
		ls.pop()
print(*sorted(set(recur(input().strip()))), sep='\n')

# 10_P14
m, a, b = map(int, input().split())
e = dict()
for _ in range(m):
	s, t = map(int, input().split())
	e.setdefault(s, []).append(t)
for k in e: e[k] = iter(e[k])
def recur(i):
	return any(map(recur, e.get(i, []))) if i < b else i == b
print(['no', 'yes'][recur(a)])

# 10_P15
m, a, b = map(int, input().split())
e = {b: [None]}
for _ in range(m):
	s, t = map(int, input().split())
	if t <= b:
		e.setdefault(s, []).append(t)
for k in e: e[k] = sorted(set(e[k]))
def trv(u, ls=[]):
	if u is None:
		yield ' -> '.join(map(str, ls))
	else:
		ls.append(u)
		for v in e.get(u, []):
			yield from trv(v)
		ls.pop()
print(*list(trv(a)) or ['no'], sep='\n')

# 10_P16
def B_to_A(trie, ls=[]):
	if not trie: yield list(ls)
	elif isinstance(trie[0], int):
		ls.append(trie[0])
		yield from B_to_A(trie[1:])
		ls.pop()
	else:
		for grp in trie:
			yield from B_to_A(grp)
print(list(B_to_A(eval(input().strip()))))

# 10_P17
def recur(con, ls=[]):
    try:
        for key, val in sorted(con.items()):
            recur(val, ls + [key])
    except:
        print('.'.join(ls), ':', con)
recur(eval(input()))

# 10_P18
import numpy as np
def read_matrix(s):
    mat = np.matrix(s.split(), dtype=np.int).reshape(4, 4) - 1
    i, j = list(zip(*np.where(mat==-1)))[0]; mat[i, j] = 15
    return mat, i, j
def heurioustic(mat):
    return sum(abs(i-vl//4) + abs(j-vl%4) for (i,j),vl in np.ndenumerate(mat)) // 2
def recur(mat, i, j, dep, track=''):
    h = heurioustic(mat)
    if not h:  return ''.join(track)
    if h > dep: return None
    for c, x, y in zip('RDLU', [i,i+1,i,i-1], [j+1,j,j-1,j]):
        if 0 <= x < 4 and 0 <= y < 4:
            mat[i,j], mat[x,y] = mat[x,y], mat[i,j]
            tmp = recur(mat, x, y, dep-1, track + c)
            mat[i,j], mat[x,y] = mat[x,y], mat[i,j]
            if tmp: return tmp
    return None
mat, i, j = read_matrix(input())
for d in range(10):
    tmp = recur(mat, i, j, d)
    if tmp:
        print(tmp)
        break
else:
    print('Cannot find answer')
