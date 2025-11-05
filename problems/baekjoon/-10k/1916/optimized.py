import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

dist = [INF] * (n+1)
dist[start] = 0

pq = [(0, start)]  # (비용, 노드)

while pq:
    cost, now = heapq.heappop(pq)

    if cost > dist[now]:
        continue

    for nxt, w in graph[now]:
        new_cost = cost + w
        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(pq, (new_cost, nxt))

print(dist[end])
