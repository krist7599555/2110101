# 04_L1
print('ddedd'[int(input()) - 1])

# 04_L2
cnt, mxx, lts = 0, 0, ' '
for ch in input().lower():
	if lts != ch:
		lts, cnt = ch, 0
	cnt += 1
	mxx = max(mxx, cnt)
print(mxx)

# 04_L3
a, b = input(), input()
s, t = map(lambda l: sorted(l.lower().replace(' ', '')), [a, b])
print(a, b if s != t else '')

# 04_L4
d, w, s, t = (input().strip() for i in range(4))
i, ans = 0, []
while i < len(w):
	if w[i:i+len(s)].lower() == s.lower():
		ans.extend(t)
		i += len(s)
		if d == 'R':
			ans.extend(w[i:])
			break
	else:
		ans.append(w[i])
		i += 1
print(*ans, sep='')
