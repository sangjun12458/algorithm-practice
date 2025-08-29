import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for next, weight in graph[current]:
            if visited[next] == - 1:
                visited[next] = visited[current] + weight
                queue.append(next)

    max_dist = max(visited)
    farthest_node = visited.index(max_dist)
    return (farthest_node, max_dist)

stopover, _ = bfs(1)
_, diameter = bfs(stopover)

print(diameter)