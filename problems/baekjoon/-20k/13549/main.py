# 13549. 숨바꼭질 3
n, k = map(int, input().split())
visited = [-1] * 100001

from collections import deque
q = deque(5)
visited[5] = 0

while visited[k]:
    start = q.popleft()


    q.append(start + 1)
    q.append(start - 1)
    q.append

    if visited[start + 1] == -1:
        visited[start + 1] = visited[start] + 1
        q.append(start + 1)
    if visited[start - 1] == -1:
        visited[start - 1] = visited[start] + 1
        q.append(start + 1)
    