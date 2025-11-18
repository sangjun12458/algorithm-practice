# 1043. 거짓말
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
knowns = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(m)]
graph = [[False] * (n + 1) for _ in range(n+1)]

for party in parties:
    for i in range(1, len(party)):
        for j in range(i + 1, len(party)):
            graph[party[i]][party[j]] = True
            graph[party[j]][party[i]] = True

visited = [False] * (n + 1)
persons = [False] * (n + 1)
q = deque()

for x in knowns[1:]:
    persons[x] = True
    visited[x] = True
    q.append(x)
while q:
    x = q.popleft()
    for y in range(1, n + 1):
        if visited[y]: continue
        if not graph[x][y]: continue
        visited[y] = True
        persons[y] = True
        q.append(y)

ans = 0
for party in parties:
    can_lie = True
    for x in party[1:]:
        if persons[x]:
            can_lie = False
    if can_lie:
        ans += 1
print(ans)