# 17143. 낚시왕

DIR = ((0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)) 
### 1. 위, 2. 아래, 3. 오른쪽, 4. 왼쪽

R, C, M = map(int, input().split())
board = [[-1] * (C) for _ in range(R)]
sharks = []
catched = [False] * 10001

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = i
    sharks.append((r-1, c-1, s, d, z))

ans = 0
for fisher in range(C):
    # catch a shark
    for row in range(R):
        shark_idx = board[row][fisher]
        if shark_idx != -1 and not catched[shark_idx]:
            ans += sharks[shark_idx][4]
            catched[shark_idx] = True
            board[row][fisher] = -1
            break

    next_pos = [[] for _ in range] # 이전 위치, 새로운 위치 모두 구한 후 갱신
    # sharks move
    for idx, (r, c, s, d, z) in enumerate(sharks):
        if catched[idx]: continue
        dr, dc = DIR[d]

        if d == 1:
            nr = 2 * R - 2 - r - s*dr
        else:
            nr = r + s*dr
        if d == 4:
            nc = 2 * C - 2 - c - s*dc
        else:
            nc = c + s*dc
        if d == 1 or d == 2:
            if nr // (R - 1) % 2 == 0:
                nr %= (R - 1)
                nd = 2
            else:
                nr = R - 1 - (nr % (R - 1))
                nd = 1
        else:
            if nc // (C - 1) % 2 == 0:
                nc %= (C - 1)
                nd = 3
            else:
                nc = C - 1 - (nc % (C - 1))
                nd = 4

        sharks[idx] = (nr, nc, s, nd, z)
    
        board[r][c] = -1
        if board[nr][nc] != -1:
            other_idx = board[nr][nc]
            other_z = sharks[other_idx][4]
            if z > other_z:
                board[nr][nc] = idx
                catched[other_idx] = True
            else:
                catched[idx] = True
        else:
            board[nr][nc] = idx

print(ans)