# 2448. 별 찍기 - 11

n = int(input())

board = [[" "] * (2 * n - 1) for _ in range(n)]

def draw(r, c, size):
    if size == 3:
        board[r][c] = "*"
        board[r+1][c-1] = board[r+1][c+1] = "*"
        for i in [-2, -1, 0, 1, 2]:
            board[r+2][c+i] = "*"
        return
    
    half = size // 2
    draw(r, c, half)
    draw(r + half, c - half, half)
    draw(r + half, c + half, half)

draw(0, n-1, n)

for i in range(n):
    print("".join(board[i]))