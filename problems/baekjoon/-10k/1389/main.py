import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [-1] * (n+1)
    q = deque([start])
    visited[start] = 0
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)
    return sum(visited[1:])  # 1~n까지 거리 합

answer = 0
min_value = int(1e9)

for i in range(1, n+1):
    result = bfs(i)
    if result < min_value:
        min_value = result
        answer = i

print(answer)
