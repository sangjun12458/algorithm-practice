# 1916. 최소비용 구하기
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().strip())
m = int(input().strip())
buses = [[-1] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    if buses[u][v] == -1:
        buses[u][v] = w
    else:
        buses[u][v] = min(buses[u][v], w)

start, end = map(int, input().split())
visited = [False] * (n + 1)
dist = [INF] * (n + 1)

dist[start] = 0
for _ in range(n):
    u = -1
    d = INF
    for i in range(1, n+1):
        if visited[i]: continue
        if d <= dist[i]: continue
        u = i
        d = dist[i]
    visited[u] = True

    for v in range(1, n+1):
        if buses[u][v] == -1: continue
        if visited[v]: continue
        dist[v] = min(dist[v], dist[u] + buses[u][v])
print(dist[end])