# 2206. 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
stage = [[ch for ch in input().strip()] for _ in range(n)]
stage[0][0] = '1'
q = deque()
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for i in range(n):
    for j in range(m):
        if stage[i][j] == '0': continue
        stage[i][j] = '0'

        q.append((i, j, 1))
        visited = [[0] * m for _ in range(n)]
        visited[i][j] = True
        while q:
            ci, cj, dist = q.popleft()
            for di, dj in dir:
                ni, nj = ci + di, cj + dj
                if ni == n-1 and nj == m-1:
                    pass
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                    q.append((ni, nj, dist + 1))

        stage[i][j] = '1'

        