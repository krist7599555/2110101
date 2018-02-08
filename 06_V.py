# 06_V1
print('x k tu c h'.split()[int(input()) - 1])

# 06_V2
grd = list(zip([80, 70, 60, 50, 0], 'ABCDF'))
ans = []
for x, n1, n2, *sc in [s.split(';') for s in open(input().strip())]:
	sc = sum(map(float, sc))
	gr = next(gr for lm, gr in grd if sc >= lm)
	ans.append([x, n1 + ' ' + n2, gr])
print(ans)

# 06_V3
grd = list(zip([80, 70, 60, 50, 0], 'ABCDF'))
dic = dict()
for x, n1, n2, *sc in [s.split(';') for s in open(input().strip()) if s.count(';') == 4]:
	sc = sum(map(float, sc))
	gr = next(gr for lm, gr in grd if sc >= lm)
	dic.setdefault(x, [x, n1 + ' ' + n2, gr])
for nm in map(str.strip, __import__('sys').stdin):
	if nm != '-1':
		print(dic.get(nm, 'Not Found'))

# 06_V4
dic, mrd = {}, {}
for ft, nm in [s.strip().split() for s in open(input().strip())]:
	dic.setdefault(ft, []).append(nm)
	if ft not in mrd:
		mrd[ft] = len(mrd)
print(sorted(map(list, dic.items()), key=lambda i: mrd[i[0]]))
print('The most favorite fruit is', max(dic.items(), key=lambda l: len(l[-1]))[0])
