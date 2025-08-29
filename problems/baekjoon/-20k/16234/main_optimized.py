# 16234. 인구 이동
import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(sx, sy, visited):
    q = deque([(sx, sy)])
    union = [(sx, sy)]
    visited[sx][sy] = True
    total_pop = nations[sx][sy]

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(nations[x][y] - nations[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total_pop += nations[nx][ny]

    if len(union) > 1:
        new_pop = total_pop // len(union)
        for x, y in union:
            nations[x][y] = new_pop
        return True
    return False

def solve():
    days = 0
    while True:
        visited = [[False]*n for _ in range(n)]
        moved = False
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    if bfs(i, j, visited):
                        moved = True
        if not moved:
            return days
        days += 1

print(solve())