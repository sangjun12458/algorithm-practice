# 17472. 다리 만들기 2
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 1. 섬 번호 매기기 (BFS)
def bfs(si, sj, idx):
    q = deque([(si, sj)])
    board[si][sj] = idx
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 1:
                board[ni][nj] = idx
                q.append((ni, nj))

island_id = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            island_id += 1
            bfs(i, j, island_id)

island_cnt = island_id - 1

# 2. 섬 사이 다리 길이 계산
edges = [[0] * island_cnt for _ in range(island_cnt)]

for i in range(n):
    for j in range(m):
        if board[i][j] > 1:        
            start = board[i][j] - 2
            for di, dj in dirs:
                ni, nj, dist = i, j, 0
                while True:
                    ni += di
                    nj += dj
                    if not (0 <= ni < n and 0 <= nj < m): break
                    if board[ni][nj] == 0:
                        dist += 1
                        continue
                    elif board[ni][nj] == board[i][j]:
                        break    
                    if dist > 1:
                        end = board[ni][nj] - 2
                        if edges[start][end] == 0 or dist < edges[start][end]:
                            edges[start][end] = dist
                            edges[end][start] = dist
                    break

# 3. Prim 알고리즘 (MST)
connected = [False] * island_cnt
connected[0] = True
result = 0

for _ in range(island_cnt - 1):
    min_dist = float('inf')
    min_node = -1
    for u in range(island_cnt):
        if not connected[u]: continue
        for v in range(island_cnt):
            if connected[v]: continue
            if 0 < edges[u][v] < min_dist:
                min_dist = edges[u][v]
                min_node = v
    if min_node == -1:
        print(-1)
        sys.exit()
    connected[min_node] = True
    result += min_dist
    
print(result)