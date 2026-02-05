# 3190. 뱀

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
DIR = ((-1, 0), (1, 0), (0, -1), (0, 1))
MAX_LEN = 10000

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
L = int(input())
rots = [''] * (MAX_LEN + 1)
for _ in range(L):
    X, C = input().split()
    rots[int(X)] = C

snake = [(0, 0, RIGHT)] # list -> linked list
game_over = False
tick = 0
while not game_over:
    tick += 1
    if tick > N + MAX_LEN:
        game_over = True
        continue

    x, y, (dx, dy) = snake[0]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < N):
        game_over = True
        continue

    if board[nx][ny] == -1:
        game_over = True
    elif board[nx][ny] == 0:
        pass
    elif board[nx][ny] == 1:
        pass

    # for x, y, dx, dy in snake:
    #     nx, ny = x + dx, y + dy
        