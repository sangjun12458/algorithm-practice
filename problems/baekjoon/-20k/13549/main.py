# 13549. 숨바꼭질 3
from collections import deque
END = int(1e5)

n, k = map(int, input().split())
visited = [-1] * (END + 1)

q = deque([k])
visited[k] = 0

while q and visited[n] == -1:
    now = q.popleft()

    next = now
    while next > 0 and not next % 2:
        next //= 2
        if visited[next] == -1:
            visited[next] = visited[now]
            q.append(next)

    for i in [-1, 1]:
        next = now + i
        if not (0 <= next <= END): continue
        if visited[next] == -1:
            visited[next] = visited[now] + 1
            q.append(next)

print(visited[n])    