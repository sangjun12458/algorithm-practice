# 1987. 알파벳
import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
DIR = [(-1, 0), (0, -1), (1, 0), (0, 1)]

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(R)]

ans = 1

loc_board = board
loc_R = R
loc_C = C
loc_DIR = DIR

def dfs(y, x, bit, depth):
    global ans
    ans = max(ans, depth)
    
    for dy, dx in loc_DIR:
        ny, nx = y + dy, x + dx
        if 0 <= ny < loc_R and 0 <= nx < loc_C:
            c = loc_board[ny][nx]
            mask = 1 << c
            if not (bit & mask):
                dfs(ny, nx, bit | mask, depth + 1)

dfs(0, 0, 1 << board[0][0], 1)
print(ans)