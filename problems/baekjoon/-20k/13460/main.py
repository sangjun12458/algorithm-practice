# 13460. 구슬 탈출 2
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
ans = 11
visited = [[11] * n * m for _ in range(n * m)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue = (i, j)
            board[i][j] = '.'

def hash(coord):
    return coord[0] * m + coord[1]

def move(red, blue, dy, dx):
    ry, rx = red
    by, bx = blue
    blocking = False
    blocked = False

    while board[ry + dy][rx + dx] == '.':
        ry += dy
        rx += dx
        if (ry, rx) == blue:
            blocked = True

    while board[by + dy][bx + dx] == '.':
        by += dy
        bx += dx
        if (by, bx) == red:
            blocking = True

    if board[ry + dy][rx + dx] != 'O' and board[by + dy][bx + dx] != 'O':
        if blocked:
            ry, rx = by - dy, bx - dx
        elif blocking:
            by, bx = ry - dy, rx - dx
    
    return (ry, rx), (by, bx)

def dfs(red, blue, depth):
    global ans
    if depth >= 10 or depth >= ans:
        return
    for dy, dx in DIR:
        new_red, new_blue = move(red, blue, dy, dx)
        if board[new_blue[0] + dy][new_blue[1] + dx] == 'O':
            continue
        if board[new_red[0] + dy][new_red[1] + dx] == 'O':
            ans = min(ans, depth + 1)
            return
        hash_r = hash(new_red)
        hash_b = hash(new_blue)
        if visited[hash_r][hash_b] < depth + 1:
            continue
        visited[hash_r][hash_b] = depth + 1
        dfs(new_red, new_blue, depth + 1)

visited[hash(red)][hash(blue)] = 0
dfs(red, blue, 0)
print(ans if ans <= 10 else -1)