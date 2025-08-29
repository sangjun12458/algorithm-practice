import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
shark = [-1, -1, -1, -1]
total_time = 0
delta = [[-1, 0], [0, -1], [0, 1], [1, 0]]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark = [i, j, 2, 0]

while True:
    feed = [-1, -1, 999]
    bfs = deque()
    visited = [[False] * n for _ in range(n)]
    bfs.append([shark[0], shark[1], 0])
    while bfs:
        now = bfs.popleft()
        if visited[now[0]][now[1]]:
            continue
        visited[now[0]][now[1]] = True
        if space[now[0]][now[1]] > 0 and space[now[0]][now[1]] < shark[2]:
            if now[2] < feed[2]:
                feed = now
            elif now[2] == feed[2]:
                if now[0] < feed[0]:
                    feed = now
                elif now[0] == feed[0]:
                    if now[1] < feed[1]:
                        feed = now
        for di, dj in delta:
            ni, nj = now[0] + di, now[1] + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n: 
                continue
            if visited[ni][nj]:
                continue
            if space[ni][nj] in range(0, shark[2]+1):
                bfs.append([ni, nj, now[2] + 1])

    if feed[0] == -1:
        break
    else:
        space[feed[0]][feed[1]] = 9
        space[shark[0]][shark[1]] = 0
        shark[0], shark[1] = feed[0], feed[1]
        shark[3] += 1
        if shark[2] == shark[3]:
            shark[2] += 1
            shark[3] = 0
        total_time += feed[2]

print(total_time)