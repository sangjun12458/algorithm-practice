# 11403. 경로 찾기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(input().split()) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            q.append((i, j))

while q:
    x, y = q.popleft()
    for z in range(n):
        if graph[y][z] == '1' and graph[x][z] == '0':
            graph[x][z] = '1'
            q.append((x, z))

for row in graph:
    print(' '.join(row))