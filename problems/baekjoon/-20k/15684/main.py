# 15684. 사다리 조작

def check():
    global ladder
    for i in range(N):
        col = i
        row = 0
        while row < H:
            if ladder[row][col] != 0:
                col += ladder[row][col]
            row += 1
        if col != i:
            return False
    return True

def dfs(depth, r, c):
    global answer, ladder
    if depth > 3:
        return

    if check():
        answer = min(depth, answer)
        return
    for i in range(r, H):
        for j in range(N-1):
            if i == r and j < c:
                continue
            if ladder[i][j] != 0:
                continue
            if ladder[i][j+1] != 0:
                continue
            ladder[i][j] = 1
            ladder[i][j+1] = -1
            dfs(depth+1, i, j)
            ladder[i][j] = 0
            ladder[i][j+1] = 0

N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = -1

answer = 10
dfs(0, 0, 0)
print(answer if answer <= 3 else -1)