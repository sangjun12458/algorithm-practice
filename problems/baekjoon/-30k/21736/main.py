# 21736. 헌내기는 친구가 필요해
import sys
input = sys.stdin.readline
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())
campus = [input().strip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            doyeon = (i, j)

q = [doyeon]
visited[doyeon[0]][doyeon[1]]
people = 0
while q:
    x, y = q.pop(0)
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < m): continue
        if campus[nx][ny] == 'X': continue
        if visited[nx][ny]: continue
        visited[nx][ny] = True
        q.append((nx, ny))
        if campus[nx][ny] == 'P':
            people += 1
print(people if people else 'TT')