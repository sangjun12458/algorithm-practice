# 17472. 다리 만들기 2
import sys
from collections import deque

input = sys.stdin.readline
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# ====== BFS island labeling ======
def bfs(i, j, label):
    q = deque([(i, j)])
    board[i][j] = label
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                board[nx][ny] = label
                q.append((nx, ny))

# ====== find bridge ======
def get_edges():
    edges = []
    for i in range(N):
        for j in range(M):
            if board[i][j] < 2: continue
            start = board[i][j]
            for di, dj in dirs:
                length = 0
                ni, nj = i + di, j + dj
                while 0 <= ni < N and 0 <= nj < M:
                    if board[ni][nj] == start: break
                    if board[ni][nj] > 1:
                        if length >= 2:
                            end = board[ni][nj]
                            edges.append((length, start ,end))
                        break
                    ni += di
                    nj += dj
                    length += 1              
    return edges

# ====== Union-Find ======
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a
        return True
    return False

# ====== main ======
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 1. island labeling
label = 2
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            bfs(i, j, label)
            label += 1

island_count = label - 2

# 2. find all the bridges
edges = get_edges()

# 3. MST (Krusukal)
edges.sort()
parent = [i for i in range(label)]

cnt, total = 0, 0
for w, a, b in edges:
    if union(a, b):
        total += w
        cnt += 1

# 4. check result
root = find(1)
if cnt == island_count - 1:
    print(total)
else:
    print(-1)