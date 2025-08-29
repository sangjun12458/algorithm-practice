# 17144. 미세먼지 안녕!
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
for i in range(R):
    if room[i][0] == -1:
        purifier = i
        break
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def diffuse():
    diffusions = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] <= 0: continue
            amount = room[i][j] // 5
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if not (0 <= ni < R and 0 <= nj < C): continue
                if room[ni][nj] == -1: continue
                diffusions[i][j] -= amount
                diffusions[ni][nj] += amount

    for i in range(R):
        for j in range(C):
            room[i][j] += diffusions[i][j]

def purify():
    top, bottom = purifier, purifier + 1
    for i in range(top-1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(bottom+1, R-1):
        room[i][0] = room[i+1][0]
    for j in range(0, C-1):
        room[0][j] = room[0][j+1]
        room[R-1][j] = room[R-1][j+1]
    for i in range(top):
        room[i][C-1] = room[i+1][C-1]
    for i in range(R-1, bottom, -1):
        room[i][C-1] = room[i-1][C-1]
    for j in range(C-1, 1, -1):
        room[top][j] = room[top][j-1]
        room[bottom][j] = room[bottom][j-1]
    room[top][1] = 0
    room[bottom][1] = 0

for _ in range(T):
    diffuse()
    purify()

print(sum(sum(row) for row in room) + 2)