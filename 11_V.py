# 11_V1
print('dbdad'[int(input()) - 1])

# 11_V2
import numpy as np
mony = np.array([.0] * 5)
item = np.array([.0] * 5)
for c in map(float, input().split()):	
hity = np.array(input().split(), dtype=np.float)
	mony += c * hity
	item += hity
x = mony.tolist().index(max(mony))
print('Sun Mon Tue Wed Thu Fri Sat'.split()[x + 1], item[x])
print(*mony)

# 11_V3
import numpy as np
def cm_to_m(x): return x / 100
def cal_bmi(x): return x[:,1] / cm_to_m(x[:,0]) ** 2
def main():
    def read_height_weight():
        return np.array([input().split() for _ in range(int(input()))], dtype=np.float)
    bmi = cal_bmi(read_height_weight())
    print('average bmi =', bmi.mean())
    print('#bmi < 18.5 =', (bmi < 18.5).sum())
exec(input())

# 11_V4
import numpy as np
def read_square_matrix():
    d = list(map(int, input().split()))
    return np.array([d] + [input().split() for _ in range(len(d)-1)], dtype=np.int)
def min_in_each_row(m):    return m.min(axis=1)
def max_in_each_column(m): return m.max(axis=0)
def diff_of_sums_of_two_diags(m):
    return abs(np.diag(m).sum() - np.diag(m[::-1,:]).sum())
def halve(m):
    return m[::2, ::2] + m[1::2, ::2] + m[::2, 1::2] + m[1::2, 1::2]
exec(input())
