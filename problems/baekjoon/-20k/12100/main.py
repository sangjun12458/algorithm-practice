# 2048 (Easy)
import sys
sys.setrecursionlimit(int(1e5))

DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def move(r, c, dr, dc):
    while 0 <= r + dr < N and 0 <= c + dc < N:
        nr, nc = r + dr, c + dc
        if board[nr][nc] == 0:
            board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
            r += dr
            c += dc
        elif board[r][c] == board[nr][nc]:
            board[r][c], board[nr][nc] = 0, 2*board[r][c]
            r += dr
            c += dc
        else:
            break

def slide(dr, dc):
    r_start = N-1 if dr == 1 else 0
    r_end = -1 if dr == 1 else N
    c_start = N-1 if dc == 1 else 0
    c_end = -1 if dc == 1 else N
    for r in range(r_start, r_end, dr if dr else 1):
        for c in range(c_start, c_end, dc if dc else 1):
            if board[r][c] == 0:
                continue
            move(r, c, dr, dc)

def dfs(depth):
    if depth == 5:
        answer = 0
        for i in range(N):
            answer = max(answer, max(board[i]))
        return
    for dr, dc in DIR:
        slide(dr, dc)
        dfs(depth+1)

dfs(0)