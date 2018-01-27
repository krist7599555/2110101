# 04_V1
print('bdccb'[int(input()) - 1])

# 04_V2
inp = input()
for c in "\"',.()":
	inp = inp.replace(c, ' ')
print(inp)

# 04_V3
import re
ls = re.split("\\ |\\.|\\,|\\'|\\\"", input().lower())
print('Found' if input().lower() in map(str.strip, ls) else 'Not Found')

# 04_V4
dic = dict(zip('0123456789', 'zero one two three four five six seven eight nine'.split()))
inp = input()
print(*(dic[i] + ('',' ')[j.isdigit() or j.isalpha()] if i in dic 
	else i for i, j in zip(inp, inp[1:] + '*')), sep ='')
