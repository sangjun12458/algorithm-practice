# 23288. 주사위 굴리기 2

import sys
from collections import deque
input = sys.stdin.readline

# 동 남 서 북
DIR = [(0,1),(1,0),(0,-1),(-1,0)]

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 주사위 (위, 북, 동, 서, 남, 아래)
dice = [1,2,3,4,5,6]

def roll(d):
    global dice
    top, north, east, west, south, bottom = dice

    if d == 0:  # 동
        dice = [west, north, top, bottom, south, east]
    elif d == 1:  # 남
        dice = [north, bottom, east, west, top, south]
    elif d == 2:  # 서
        dice = [east, north, bottom, top, south, west]
    elif d == 3:  # 북
        dice = [south, top, east, west, bottom, north]

def bfs(y, x):
    visited = [[0]*M for _ in range(N)]
    q = deque([(y, x)])
    visited[y][x] = 1
    num = board[y][x]
    cnt = 1

    while q:
        cy, cx = q.popleft()
        for dy, dx in DIR:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and board[ny][nx] == num:
                    visited[ny][nx] = 1
                    cnt += 1
                    q.append((ny, nx))
    return cnt

y, x, d = 0, 0, 0
answer = 0

for _ in range(K):
    dy, dx = DIR[d]
    ny, nx = y + dy, x + dx

    # 경계
    if not (0 <= ny < N and 0 <= nx < M):
        d = (d + 2) % 4
        dy, dx = DIR[d]
        ny, nx = y + dy, x + dx

    # 이동
    y, x = ny, nx
    roll(d)

    # 점수
    B = board[y][x]
    C = bfs(y, x)
    answer += B * C

    # 방향 결정
    A = dice[5]  # 바닥
    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d - 1) % 4

print(answer)
