# 07_L1
print('j k g tu n'.split()[int(input()) - 1])

# 07_2
print(sorted(map(int, input().split())))

# 07_L3
ls = sorted(map(int, input().split())); md = (len(ls) - 1) // 2
print(sum(ls[md:len(ls)-md]) / (1 if len(ls) & 1 else 2))

# 07_L4
import sys
data = dict()
def A(a, b, c): data[a] = [a, b, int(c)]; return data[a]
def D(a): del data[a]; return a + ' deleted'
def U(a, b): data[a][-1]  = int(b); return data[a]
def T(a, b): data[a][-1] += int(b); return data[a]
def Q(): print('Bye!'); sys.exit(0)
for ln in open('inventory.txt'): A(*ln.split(';'))
for	cmd, *tp in filter(bool, map(str.split, sys.stdin)):
	if cmd is 'Q': Q()
	if (cmd is 'A') == (tp[0] in data): 
	  print(['Product code does not exist.','Duplicate product code.'][cmd is 'A'])
	else: print(globals()[cmd](*tp))
