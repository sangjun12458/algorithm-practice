# 15684. 사다리 조작

def check():
    global ladder
    for i in range(N):
        col = i
        row = 0
        passed = False
        while row < H:
            if ladder[row][col] == 0 or passed:
                passed = False
            else:
                col += ladder[row][col]
                passed = True
            row += 1
        if col != i:
            return False 
    return True

def dfs():
    return

N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = -1

for row in ladder:
    print(*row)