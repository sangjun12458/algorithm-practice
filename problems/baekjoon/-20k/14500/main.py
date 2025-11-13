# 14500. 테트로미노
import sys
input = sys.stdin.readline
DIR = [(0, -1), (-1, 0), (0, 1), (1, 0)]

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
tetromino = []
result = 0
cnt = 0

def DFS(depth):
    if depth == 4:
        global result
        result = max(result, sum(paper[r][c] for r, c in tetromino))
        return

    for x, y in tetromino:
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m): continue
            if 4 - depth <= visited[nx][ny]: continue
            tetromino.append((nx, ny))
            visited[nx][ny] = 4 - depth
            DFS(depth + 1)
            visited[nx][ny] = 0
            tetromino.pop()

for i in range(n):
    for j in range(m):
        tetromino.append((i, j))
        visited[i][j] = 4
        DFS(1)
        tetromino.clear()

print(result)