import sys
input = sys.stdin.readline

DIR = [(-1,0),(1,0),(0,-1),(0,1)]

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x)-65, input().strip())) for _ in range(R)]

ans = 0
stack = [(0, 0, 1 << board[0][0], 1)]

while stack:
    y, x, bit, depth = stack.pop()
    if depth > ans:
        ans = depth

    for dy, dx in DIR:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < R and 0 <= nx < C:
            c = board[ny][nx]
            mask = 1 << c
            if not (bit & mask):
                stack.append((ny, nx, bit | mask, depth + 1))

print(ans)