# 7569. 토마토
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

unripens = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 0:
                unripens.append((i, j, k))

result = 0
while True:
    ripens = []
    print(unripens)
    for i, j, k in unripens:
        is_ripen = False
        print(i, j, k)
        for di, dj, dk in dirs:
            if is_ripen: continue
            ni, nj, nk = i + di, j + dj, k + dk
            if not (0 <= ni < h): continue
            if not (0 <= nj < n): continue
            if not (0 <= nk < m): continue
            if tomatoes[ni][nj][nk] == 1:
                unripens.remove((i, j, k))
                ripens.append((i, j, k))
                is_ripen = True

    if len(ripens) == 0:
        if len(unripens) == 0:
            print(result)
        else:
            print(-1)
        break

    result += 1
    for i, j, k in ripens:
        tomatoes[i][j][k] = 1

    print()
    for rc in tomatoes:
        for row in rc:
            print(row)
