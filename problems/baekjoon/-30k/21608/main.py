# 21608. 상어 초등학교
import sys
input = sys.stdin.readline

N = int(input())
preferred = [0] * N * N
order = []
for _ in range(N*N):
    x, y1, y2, y3, y4 = map(int, input().split())
    preferred[x-1] = (y1, y2, y3, y4)
    order.append(x-1)

seats = [[-1] * N for _ in range(N)]
for x in order:
    r, c, satisfaction = 0, 0, 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i + di, j + dj
                if not (0 <= ni < N and 0 <= nj < N):
                    continue
                if seats[ni][nj] in preferred[x]:
                    cnt += 1
            if cnt > satisfaction or seats[r][c] != -1:
                r, c, satisfaction = i, j, cnt
    seats[r][c] = x
print(seats)