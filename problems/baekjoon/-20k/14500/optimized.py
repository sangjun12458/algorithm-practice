# 14500. 테트로미노 (최적화)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0] * m for _ in range(n)]
ans = 0

def dfs(x, y, depth, total):
    global ans
    # 가지치기: 남은 칸이 모두 최대값이라도 ans를 못 넘으면 종료
    if ans >= total + (4 - depth) * max_val:
        return
    if depth == 4:
        ans = max(ans, total)
        return
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = 0

def check_t(x, y):
    global ans
    # 중심을 기준으로 주변 4칸 중 3칸을 선택
    s = board[x][y]
    wings = []
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            wings.append(board[nx][ny])
    if len(wings) >= 3:
        wings.sort(reverse=True)
        ans = max(ans, s + sum(wings[:3]))

max_val = max(map(max, board))
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visited[i][j] = 0
        check_t(i, j)

print(ans)