# 1699. 제곱수의 합
import math

n = int(input().strip())
m = int(math.sqrt(n))
bfs = [-1] * (n + 1)
bfs[0] = 0
cnt = 0

while bfs[n] == -1:
    temp = []
    for i in range(n):
        if bfs[i] != cnt:
            continue
        for j in range(1, m+1):
            x = i + j**2
            if x > n:
                continue
            if bfs[x] > 0:
                continue
            bfs[x] = cnt + 1
    cnt += 1

print(bfs[n])