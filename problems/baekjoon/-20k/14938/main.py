# 14938. 서강그라운드
import sys
input = sys.stdin.readline
INF = 10**6

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
roads = [[INF] * (n + 1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    roads[a][b] = roads[b][a] = l

ans = 0
for start in range(1, n+1):
    distance = [INF] * (n + 1)
    visited = [False] * (n + 1)
    distance[start] = 0

    for _ in range(n):
        cur_node = 0
        for i in range(1, n+1):
            if not visited[i] and distance[i] < distance[cur_node]:
                cur_node = i
        visited[cur_node] = True

        for i in range(1, n+1):
            distance[i] = min(distance[i], distance[cur_node] + roads[cur_node][i])

    cnt = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            cnt += items[i]
    ans = max(ans, cnt)

print(ans)