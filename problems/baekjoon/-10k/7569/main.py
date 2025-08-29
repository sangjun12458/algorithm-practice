# 7569. 토마토
import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 1:
                q.append((i, j, k))

while q:
    i, j, k = q.popleft()
    for di, dj, dk in dirs:
        ni, nj, nk = i + di, j + dj, k + dk
        if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m:
            if tomatoes[ni][nj][nk] == 0:
                tomatoes[ni][nj][nk] = tomatoes[i][j][k] + 1
                q.append((ni, nj, nk))

max_day = 0
for box in tomatoes:
    for row in box:
        if 0 in row:
            print(-1)
            sys.exit(0)
        max_day = max(max_day, max(row))

print(max_day - 1)