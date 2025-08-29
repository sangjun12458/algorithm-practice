# 2206. 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
stage = [input().strip() for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    x, y, broken = q.popleft()

    if x == n - 1 and y == m - 1:
        print(visited[x][y][broken])
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue

        if stage[nx][ny] == '0' and visited[nx][ny][broken] == 0:
            visited[nx][ny][broken] = visited[x][y][broken] + 1
            q.append((nx, ny, broken))

        if stage[nx][ny] == '1' and broken == 0 and visited[nx][ny][1] == 0:
            visited[nx][ny][1] = visited[x][y][broken] + 1
            q.append((nx, ny, 1))
else:
    print(-1)