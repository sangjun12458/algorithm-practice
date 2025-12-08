# 1389. 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
fri = [[]*(n+1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    fri[a].append(b)
    fri[b].append(a)

def BFS(start):
    visited = [-1] * (n+1)
    q = deque([start])
    visited[start] = 0
    while q:
        now = q.popleft()
        for nxt in fri[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)
    return sum(visited[1:])

ans = 10**6
min_v = 0
for i in range(1, n+1):
    result = BFS(i)
    if result < ans:
        ans = result
        min_v = i

print(min_v)