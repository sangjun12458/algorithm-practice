# 14940. 쉬운 최단거리
import sys
from collections import deque

input = sys.stdin.readline
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
q = deque()

n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
distances = [[0] * m for _ in range(n)]

for i in range(n):
    if arr[i].count('2') > 0:
        q.append((i, arr[i].index('2')))

while q:
    x, y = q.popleft()
    for dx, dy in DIR:
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if arr[nx][ny] != '1' or distances[nx][ny] != 0:
            continue
        q.append((nx, ny))
        distances[nx][ny] = distances[x][y] + 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == '1' and distances[i][j] == 0:
            distances[i][j] = -1

for row in distances:
    print(" ".join(map(str, row)))