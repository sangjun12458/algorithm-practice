# 3190. 뱀
from collections import deque

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
MAX_LEN = 10000

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
L = int(input())
rots = [0] * (MAX_LEN + 1)
for _ in range(L):
    X, C = input().split()
    rots[int(X)] = -1 if C == 'L' else 1

head = (0, 0, RIGHT)
board[head[0]][head[1]] = -1
body = deque() # list -> linked list
game_over = False
tick = 0
while not game_over:
    # print()
    # print(tick)
    # for row in board:
    #     print(row)
    # print()

    tick += 1
    if tick > N + MAX_LEN:
        game_over = True
        continue

    x, y, d = head
    dx, dy = DIR[d]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < N):
        game_over = True
        continue

    head = (nx, ny, (d+rots[tick])%4)
    body.appendleft((x, y))
    if board[nx][ny] == -1:
        tx, ty = body.pop()
        board[tx][ty] = 0
        if board[nx][ny] == -1:
            game_over = True
    else:
        if board[nx][ny] == 0:
            tx, ty = body.pop()
            board[tx][ty] = 0
    board[nx][ny] = -1

print(tick)