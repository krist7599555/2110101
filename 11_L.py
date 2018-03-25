# 11_L1
print('acbcb'[int(input()) - 1])

# 11_L2
import numpy as np
assert np.newaxis is None
def all_pair_distances(p):
	x, y = p[:, 0], p[:, 1]
	dx = x - x[:, np.newaxis]
	dy = y - y[:, np.newaxis]
	return np.hypot(dx, dy)
exec(input().strip())

# 11_L3
import numpy as np
def eval_poly(x, w):
	return np.dot(w, x ** np.arange(len(w)))
exec(input())

# 11_L4
import numpy as np
def checker(n):
    return np.array([[(i ^ j) & 1 for j in range(n)] for i in range(n)])
def collide(e, ls):
    def intersect(a, b):
        return np.hypot(a[0] - b[0], a[1] - b[1]) <= a[2] + b[2]
    return ls[np.array([intersect(e, it) for it in ls])]
def matrix_chain_mult(m, o):
    nw = m[o[0]]
    for i in o[1:]:
        nw = np.matmul(m[i], nw) if i < o[0] else np.matmul(nw, m[i])
    return nw
exec(input())
