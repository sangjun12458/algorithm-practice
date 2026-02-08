# 17143. 낚시왕

R, C, M = map(int, input().split())
board = [[False] * (C+1) for _ in range(R+1)]
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c] = True
    sharks.append((r, c, s, d, z))

ans = 0
for fisher in range(1, C+1):
    # catch a shark
    for row in range(1, R+1):
        if board[row][fisher]:
            

    # sharks move
    for r, c, s, d, z in sharks:
        # need to calculate next pos
        nr = r
        nc = c

    