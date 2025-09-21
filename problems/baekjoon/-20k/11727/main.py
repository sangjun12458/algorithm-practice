# 11727. 2×n 타일링 2
CONST = 10007

n = int(input().strip())
tiling = [0] * (n + 1)
tiling[1] = 1
tiling[2] = 3
for i in range(3, n + 1):
    tiling[i] = (tiling[i - 1] + tiling[i - 2] * 2) % CONST

print(tiling[n])