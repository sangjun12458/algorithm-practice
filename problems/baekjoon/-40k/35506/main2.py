N = int(input())

size = 2 * N
board = [[' '] * size for _ in range(size)]

# 위쪽 X
for i in range(N):
    board[i][i] = '*'
    board[i][size - i - 1] = '*'

# 아래쪽 X
for i in range(N):
    board[N + i][i] = '*'
    board[N + i][size - i - 1] = '*'

# 출력
for row in board:
    print(''.join(row))
