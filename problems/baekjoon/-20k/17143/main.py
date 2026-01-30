# 17143. 낚시왕

R, C, M = map(int, input().split())
board = [[0] * (C+1) for _ in range(R+1)]
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c] = 1
    sharks.append((r, c, s, d, z))
    