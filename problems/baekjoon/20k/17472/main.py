import sys
from collections import deque

def new_print(m):
    print("map")
    for row in m:
        print(" ".join(map(str, row)))

input = sys.stdin.readline
n, m = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dij = [(-1, 0), (1, 0), (0, -1), (0, 1)]

numbering = 1
for i in range(n):
    for j in range(m):
        if country[i][j] != 1:
            continue 

        numbering += 1
        q.append((i, j))

        while q:
            nowi, nowj = q.popleft()
            country[nowi][nowj] = numbering
            for di, dj in dij:
                newi = nowi + di
                newj = nowj + dj
                if newi < 0 or newi >= n or newj < 0 or newj >= m:
                    continue
                if country[newi][newj] == 1:
                    q.append((newi, newj))

nodes = [0] * (numbering - 1)
edges = []

for i in range(n):
    for j in range(m):
        island = country[i][j]
        if island <= 1: continue
        for di, dj in dij:
            ni = i + di
            nj = j + dj