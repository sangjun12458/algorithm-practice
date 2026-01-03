# 16724. 피리 부는 사나이
import sys
input = sys.stdin.readline
delta = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}

N, M = map(int, input().split())
dirs = [input().strip() for _ in range(N)]

group = [[0] * M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if group[i][j] != 0: continue
        cnt += 1
        group[i][j] = cnt

        now = (i, j)
        dir = dirs[i][j]
        new = delta[dir]

