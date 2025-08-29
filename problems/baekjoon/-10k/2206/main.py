# 2206. 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
stage = [[ch for ch in input().strip()] for _ in range(n)]
q = deque()
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
visited = [[0] * m for _ in range(n)]

q.append((0, 0, 1, 0))
visited[0][0] = 1

result = []
while q:
    i, j, dist, used_broken = q.popleft()
    v = visited[i][j]

    if i == n-1 and j == m-1:
        result.append(dist)
        break

    for di, dj in dir:
        ni, nj = i + di, j + dj
        if not (0 <= ni < n and 0 <= nj < m): continue
        nv = visited[ni][nj]

        if stage[ni][nj] == '0':
            if nv == 0:
                visited[ni][nj] = used_broken + 1
                q.append((ni, nj, dist+1, used_broken))
            elif nv == 2:
                if not used_broken:
                    visited[ni][nj] = 1
                    q.append((ni, nj, dist+1, 0))
        elif stage[ni][nj] == '1':
            if nv == 0:
                if not used_broken:
                    visited[ni][nj] = 2
                    q.append((ni, nj, dist+1, 1))

if result:
    print(result[0])
else:
    print(-1)