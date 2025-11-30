# 14502. 연구소
from collections import deque
DIR = ((0, -1), (0, 1), (-1, 0), (1, 0))

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
viruses = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            viruses.append((i, j))
ans = 0

def bfs():
    global ans

    q = deque(viruses)
    temp_lab = [row[:] for row in lab]
    while q:
        x, y = q.popleft()
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if temp_lab[nx][ny] != 0:
                continue
            temp_lab[nx][ny] = 2
            q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_lab[i][j] == 0:
                cnt += 1                
    ans = max(ans, cnt)

def dfs(pi, pj, depth):
    if depth == 3:
        bfs()
    else:
        pa = pi * m + pj
        for a in range(pa, n*m):
            wi, wj = a // m, a % m
            if lab[wi][wj] != 0:
                continue
            lab[wi][wj] = 1
            dfs(wi, wj, depth+1)
            lab[wi][wj] = 0

dfs(0, 0, 0)
print(ans)