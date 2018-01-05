# 02_L1
print('edcbe'[int(input())-1])

# 02_L2
print(sorted([int(input()) for _ in range(5)])[2])

# 02_3
nm = int(input())
if nm < 0 or nm > 80:
	print('Error : Out of range')
else:
	ls = [0] * 4
	for i in range(4):
		ls[i] = nm % 3
		nm //= 3
	print(*ls[::-1], sep='')
  
  
# 02_L4
import math

def ems(nm):
	ls = [32, 37, 42, 52, 67, 82, 97, 122, 137, 157, 177, 197, 217, 242, 267, 292, 317, 342, 367, 397, 427, 457, 487];
	cs = [20, 100, 250, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
	return next((cst for lm, cst in zip(cs, ls) if nm <= lm), 'ERROR')

def rgs(nm):
	ls = [18, 22, 28, 38, 58];
	cs = [100, 250, 500, 1000, 2000]
	return next((cst for lm, cst in zip(cs, ls) if nm <= lm), 'ERROR')
  
def nrm(nm):
	return 5 + 15 * math.ceil(nm / 1e3)

cm = input().strip()
nm = int(input())
print({'N':nrm, 'E':ems, 'R':rgs}[cm](nm) if nm > 0 else 'ERROR')
