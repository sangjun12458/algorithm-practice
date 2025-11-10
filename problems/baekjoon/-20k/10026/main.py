# 10026. 적록색약
from collections import deque
DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]

n = int(input())
drawing = [input() for _ in range(n)]
area = [[0] * n for _ in range(n)]

idx = 0
for i in range(n):
    for j in range(n):
        if area[i][j] != 0: continue
        idx += 1
        area[i][j] = idx
        q = deque([(i, j)])
        while q:
            x, y = q.popleft()
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n): continue
                if area[nx][ny] == 0 and drawing[x][y] == drawing[nx][ny]:
                    area[nx][ny] = idx
                    q.append((nx, ny))

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]: continue
        visited[i][j] = True
        q = deque([(i, j)])
        while q:
            x, y = q.popleft()
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n): continue
                if area[x][y] == area[nx][ny]: continue
                if drawing[x][y] in ['R', 'G'] and drawing[nx][ny] in ['R', 'G']:
                    area[nx][ny] = area[x][y]
                    q.append((nx, ny))
                    visited[nx][ny]

s = set()
for row in area:
    s = s.union(set(row))
print(idx, len(s))