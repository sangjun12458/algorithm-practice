# 16724. 피리 부는 사나이
import sys
input = sys.stdin.readline
delta = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}

N, M = map(int, input().split())
dirs = [input().strip() for _ in range(N)]

group = [[0] * M for _ in range(N)]
parent = [0]

def find_root(x):
    if parent[x] == x:
        return x
    else:
        return find_root(parent[x])

def union(a, b):
    r1 = find_root(a)
    r2 = find_root(b)
    if r1 < r2:
        parent[r2] = r1
    else:
        parent[r1] = r2

cnt = 0
for i in range(N):
    for j in range(M):
        if group[i][j] != 0: continue
        r, c = i, j
        cnt += 1
        parent.append(cnt)
        while group[r][c] == 0:
            group[r][c] = cnt
            dr, dc = delta[dirs[r][c]]
            r, c = r + dr, c + dc
        union(cnt, group[r][c])

s = set()
for p in parent[1:]:
    s.add(p)
print(len(s))