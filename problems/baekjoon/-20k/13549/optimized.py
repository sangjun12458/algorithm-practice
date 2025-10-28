# 13549. 숨바꼭질 3 (0-1 BFS)
from collections import deque

n, k = map(int, input().split())
MAX = 100000
INF = int(1e9)

dist = [INF] * (MAX + 1)
dist[n] = 0

q = deque([n])

while q:
    x = q.popleft()
    if x == k:
        print(dist[x])
        break

    nx = x * 2
    if nx <= MAX and dist[nx] > dist[x]:
        dist[nx] = dist[x]
        q.appendleft(nx)

    for nx in (x - 1, x + 1):
        if 0 <= nx <= MAX and dist[nx] > dist[x] + 1:
            dist[nx] = dist[x] + 1
            q.append(nx)