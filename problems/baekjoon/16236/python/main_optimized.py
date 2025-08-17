import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            sx, sy = i, j
            space[i][j] = 0

size, eaten, total_time = 2, 0, 0
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
visited = [[0]*n for _ in range(n)]
time_stamp = 0

def bfs(x, y, size):
    global visited, time_stamp
    time_stamp += 1

    q = deque([(x, y, 0)])
    visited[x][y] = time_stamp
    fish = []

    while q:
        i, j, d = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] != time_stamp:
                if space[ni][nj] <= size:
                    visited[ni][nj] = time_stamp
                    if 0 < space[ni][nj] < size:
                        fish.append((d+1, ni, nj))
                    else:
                        q.append((ni, nj, d+1))
    if not fish:
        return None
    else:
        return min(fish)

while True:
    res = bfs(sx, sy, size)
    if res is None:
        break
    dist, fx, fy = res
    total_time += dist
    sx, sy = fx, fy
    space[fx][fy] = 0
    eaten += 1
    if size == eaten:
        size += 1
        eaten = 0

print(total_time)