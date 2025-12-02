# 2638. 치즈
import sys
input = sys.stdin.readline
DIR = ((0,-1),(0,1),(-1,0),(1,0))

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

outside = []
for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j == m-1:
            grid[i][j] = -1
            outside.append((i, j))
        elif grid[i][j] == 1:
            cnt += 1

ans = 0
while cnt > 0:
    ans += 1

    # outside air
    while outside:
        oi, oj = outside.pop()
        for di, dj in DIR:
            ni, nj = oi + di, oj + dj
            if not (0 <= ni < n and 0 <= nj < m):
                continue
            if grid[ni][nj] != 0:
                continue
            grid[ni][nj] = -1
            outside.append((ni, nj))

    # cheese melt
    melting_cheeses = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 1:
                continue
            num_empty = 0
            for di, dj in DIR:
                ni, nj = i + di, j + dj
                if grid[ni][nj] == -1:
                    num_empty += 1
            if num_empty >= 2:
                melting_cheeses.append((i, j))

    for ci, cj in melting_cheeses:
        grid[ci][cj] = -1
        outside.append((ci, cj))
        cnt -= 1

print(ans)