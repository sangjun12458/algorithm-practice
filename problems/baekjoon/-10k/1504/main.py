# 1504. 특정한 최단 경로
#1 -> v1 or v2 -> v2 or v1 -> n
import sys
import heapq
input = sys.stdin.readline
INF = int(10e6)

n, e = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = graph[b][a] = c
v1, v2 = map(int, input().split())

pq = []
dist = [[INF] * (n+1) for _ in range(2)]

for idx, start in enumerate([v1, v2]):
    dist[idx][start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        d, u = heapq.heappop(pq)
        for v in range(1, n+1):
            c = graph[u][v]
            if c == 0:
                continue
            if d + c < dist[idx][v]:
                dist[idx][v] = d + c
                heapq.heappush(pq, (dist[idx][v], v))

route1 = [dist[0][1], dist[0][v2], dist[1][n]]
route2 = [dist[1][1], dist[1][v1], dist[0][n]]
if INF in route1:
    if INF in route2:
        print(-1)
    else:
        print(sum(route2))
else:
    if INF in route2:
        print(sum(route1))
    else:
        print(min(sum(route1), sum(route2)))