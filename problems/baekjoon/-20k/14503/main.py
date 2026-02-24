# 14503. 로봇 청소기

DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# 0 북, 1 동, 2 남, 3 서

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
# 0 빈 칸, 1 벽, 2 청소
answer = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        answer += 1

    nd = -1
    for i in range(4):
        dr, dc = DIR[(d + i) % 4]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if room[nr][nc] == 0:
            nd = (d + i) % 4

    if nd != -1:
        dr, dc = DIR[nd]
        r, c, d = r + dr, c + dc, nd
        continue

    br, bc = DIR[(d + 2) % 4]
    back_r, back_c = r + br, c + bc
    if not (0 <= back_r < N and 0 <= back_c < M):
        break
    if room[back_r][back_c] != 2:
        break    
    r, c = back_r, back_c
        
print(answer)