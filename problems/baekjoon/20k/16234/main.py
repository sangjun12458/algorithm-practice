# 16234. 인구 이동
import sys
from collections import deque
input = sys.stdin.readline
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, l, r = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]

def solve():
    # 연합인지 확인, 연합 라벨링, 국가 개수 카운팅, 국가 인구수 합계
    labels = [[0] * n for _ in range(n)]
    counts = [0] * (n * n + 1)
    populations = [0] * (n * n + 1)
    q = deque()
    label = 0
    for i in range(n):
        for j in range(n):
            if labels[i][j] != 0: continue 
            label += 1
            labels[i][j] = label
            q.append((i, j))
            counts[label] += 1
            populations[label] += nations[i][j]
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < n): continue
                    if labels[nx][ny] != 0: continue
                    if l <= abs(nations[x][y] - nations[nx][ny]) <= r:
                        labels[nx][ny] = label
                        q.append((nx, ny))
                        counts[label] += 1
                        populations[label] += nations[nx][ny]

    if label == n * n:
        result = False
    else:
        for i in range(n):
            for j in range(n):
                nations[i][j] = populations[labels[i][j]] // counts[labels[i][j]]
        result = True

    return result

def check_border():
    return

def migrate():
    return


cnt = 0
while True:
    result = solve()
    if result:
        cnt += 1
    else:
        break

print(cnt)
