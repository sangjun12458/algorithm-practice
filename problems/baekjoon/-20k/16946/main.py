# 16946. 벽 부수고 이동하기 4
import sys
input = sys.stdin.readline
DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

label = 0
cnt = [0]
for i in range(N):
    for j in range(M):
        if board[i][j] != '0' or visited[i][j] != 0:
            continue

        label += 1
        stack = [(i, j)]
        visited[i][j] = label
        cnt.append(1)

        while stack:
            x, y = stack.pop()
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                if board[nx][ny] != '0' or visited[nx][ny] != 0:
                    continue
                stack.append((nx, ny))
                visited[nx][ny] = label
                cnt[-1] += 1

for i in range(N):
    for j in range(M):
        if board[i][j] != '1':
            continue
        s = set()
        for di, dj in DIR:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            s.add(visited[ni][nj])
        total = 1
        for l in s:
            total += cnt[l]
        new_str = board[i][:j] + str(total % 10) + board[i][j+1:]
        board[i] = new_str

for row in board:
    print(row)