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
    print()
    for row in board:
        print(row)

    # catch a shark
    for row in range(R):
        shark_idx = board[row][fisher]
        if shark_idx != -1 and not catched[shark_idx]:
            ans += sharks[shark_idx][4]
            catched[shark_idx] = True
            board[row][fisher] = -1
            break

    # sharks move
    for idx, (r, c, s, d, z) in enumerate(sharks):
        if catched[idx]: continue
        dr, dc = DIR[d]
        dr = (s * dr) % (2 * (R-1))
        dc = (s * dc) % (2 * (C-1))

        nr, nc = r + s*dr, c + s*dc
        nd = d
        if not (0 <= nr < R):
            nr = 2 * R - nr - 2 if nr >= R else -nr
            nd = (d + 1) % 2 + 1
        if not (0 <= nc < C):
            nc = 2 * C - nc - 2 if nc >= C else -nc
            nd = (d + 1) % 2 + 3
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