# 02_V1
print('aeebc'[int(input())-1])

# 02_V2
print(*sorted(int(input()) for _ in range(4)))

# 02_V3
ls = list(float(input()) for _ in range(6))
print(min(ls), max(ls))

# 02_V4
d = int(input())
m = int(input())
y = int(input()) - 543
mnt = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mnt[1] = 29 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 28
print(d + sum(mnt[:m-1]))
