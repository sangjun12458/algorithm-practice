# 19236. 청소년 상어
from collections import deque
DIR = [(0, 0), 
       (-1, 0), (-1, -1), (0, -1), (1, -1),
       (1, 0), (1, 1), (0, 1), (-1, 1)]

def move_fish(space):
    fishes = [(-1, -1, 0)] * 17
    for i in range(4):
        for j in range(4):
            fishes[space[i][j][0]] = (i, j, space[i][j][1])
    for x, y, d in fishes:
        if d == 0:
            continue
        while True: 
            nx, ny = x + DIR[d][0], y + DIR[d][1]
            if 0 <= nx < 4 and 0 <= ny < 4 and space[nx][ny] >= 0:
                space[x][y], space[nx][ny] = space[nx][ny], space[x][y]
                break
            else:
                d = d & 8 + 1

def move_shark(space):
    for i in range(4):
        for j in range(4):
            if space[i][j][0] == -1:
                sx, sy, sd = i, j, space[i][j][1]
    
    while True:
        dx, dy = DIR[sd]
        nx, ny = sx + dx, sy + dy

    return

def dfs():
    pass

space = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    row = []
    for j in range(0, 8, 2):
        row.append((space[i][j], space[i][j+1]))
    space[i] = row
ans = space[0][0][0]
space[0][0] = (-1, space[0][0][1])



print(space, ans)
