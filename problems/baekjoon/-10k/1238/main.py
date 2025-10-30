# 1238. 파티
import sys
input = sys.stdin.readline
INF = int(1e6)
FRONT = 0
BACK = 1

n, m, x = map(int, input().split())
town = [[0] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    town[u][v] = w

visited = [[False, False] for _ in range(n+1)]
dist = [[INF, INF] for _ in range(n+1)]
dist[x][FRONT] = dist[x][BACK] = 0

for _ in range(n):
    for dir in [FRONT, BACK]:
        # 1. select start node
        start = -1
        d = INF
        for i in range(1, n+1):
            if visited[i][dir]: continue
            if d < dist[i][dir]: continue
            start = i
            d = dist[i][dir]
        visited[start][dir] = True
        
        # 2. update dist
        for end in range(1, n+1):
            if dir == FRONT:
                if town[start][end] == 0: continue
            else:
                if town[end][start] == 0: continue
            if visited[end][dir]: continue
            if dir == FRONT:
                dist[end][dir] = min(dist[end][dir], dist[start][dir] + town[start][end])
            else:
                dist[end][dir] = min(dist[end][dir], dist[start][dir] + town[end][start])

result = 0
for i in range(1, n+1):
    result = max(result, sum(dist[i]))
    if result < sum(dist[i]):
        result = sum(dist[i])
print(result)