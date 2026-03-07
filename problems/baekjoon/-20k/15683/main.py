# 15683. 감시
import copy
DIR = ((-1, 0), (0, -1), (1, 0), (0, 1))

class cctv:
    def __init__(self, t, r, c, d):
        self.t = t
        self.r = r
        self.c = c
        self.d = d

def dfs(depth):
    global answer

    if depth == len(cctvs):
        board = copy.deepcopy(office)
        for cctv in cctvs:
            if cctv.t == 1:
                targets = [cctv.d]
            elif cctv.t == 2:
                targets = [cctv.d, cctv.d + 2]
            elif cctv.t == 3:
                targets = [cctv.d, cctv.d + 1]
            elif cctv.t == 4:
                targets = [cctv.d, cctv.d + 1, cctv.d + 2]
            else:
                targets = [0, 1, 2, 3]
                
            for i in targets:
                i %= 4
                dr, dc = DIR[i]
                nr, nc = cctv.r + dr, cctv.c + dc
                while 0 <= nr < N and 0 <= nc < M:
                    if board[nr][nc] == 0:
                        board[nr][nc] = '#'
                    elif board[nr][nc] == 6:
                        break
                    nr += dr
                    nc += dc

        cnt = 0
        for row in board:
            cnt += row.count(0)
        answer = min(cnt, answer)
        return

    t = cctvs[depth].t
    if t == 5:
        dfs(depth + 1)
    elif t == 2:
        for i in range(2):
            cctvs[depth].d = i
            dfs(depth + 1)
    else:
        for i in range(4):
            cctvs[depth].d = i
            dfs(depth + 1)

N, M = map(int, input().split())
office = list(list(map(int, input().split())) for _ in range(N))
cctvs = []
answer = N * M

for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append(cctv(office[i][j], i, j, 0))

dfs(0)
print(answer)