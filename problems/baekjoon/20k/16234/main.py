# 16234. 인구 이동
import sys
from collections import deque
input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, l, r = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]

def solve():
    labels = [[0] * n for _ in range(n)]
    q = deque()
    label = 0
    pops = []
    counts = []

    for i in range(n):
        for j in range(n):
            if labels[i][j] != 0: 
                continue 
            label += 1
            q.append((i, j))
            labels[i][j] = label
            total_pop = nations[i][j]
            cnt = 1
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < n): continue
                    if labels[nx][ny] != 0: continue
                    if l <= abs(nations[x][y] - nations[nx][ny]) <= r:
                        labels[nx][ny] = label
                        q.append((nx, ny))
                        total_pop += nations[nx][ny]
                        cnt += 1
            pops.append(total_pop)
            counts.append(cnt)

    if label == n * n:
        return False
    
    for i in range(n):
        for j in range(n):
            g = labels[i][j] - 1
            nations[i][j] = pops[g] // counts[g]

    return True

cnt = 0
while solve():
    cnt += 1

print(cnt)