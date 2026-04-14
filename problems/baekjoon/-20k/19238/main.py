# 19238. 스타트 택시
from collections import deque
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MAX_D = 1000

N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
taxi_r, taxi_c = map(lambda x: int(x)-1, input().split())

passengers = {}
for _ in range(M):
    sy, sx, ey, ex = map(lambda x: int(x)-1, input().split())
    passengers[(sy, sx)] = (ey, ex)

def cal_distance(sr, sc, end_r, end_c):
    visited = [[-1] * N for _ in range(N)]
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        dist = visited[r][c]

        
        if r == end_r and c == end_c:
            return d
        if visited[r][c]:
            continue
        visited[r][c] = True
        for dr, dc in DIR:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if arr[nr][nc]:
                continue
            q.append((nr, nc, d + 1))
    return MAX_D

proccessed = [False] * M
for _ in range(M):
    # 택시로부터 최단거리 승객 찾기
    target, best_d = -1, MAX_D
    for i in range(M):
        if proccessed[i]:
            continue
        start_r, start_c, _, _ = customer[i]
        d = cal_distance(taxi_r, taxi_c, start_r, start_c)
        if d < best_d:
            target = i
            best_d = d
    if target == -1: # 승객에게 갈 수 없으므로 종료
        gas = -1
        break
    gas -= best_d
    # 출발지에서 목적지까지 최단거리
    sr, sc, er, ec = customer[target]
    gas_used = cal_distance(sr, sc, er, ec)
    if gas_used == -1 or gas_used > gas: # 길이 없거나 연료가 부족하여 종료
        gas = -1
        break
    gas += gas_used
    taxi_r, taxi_c = er, ec
    proccessed[target] = True

print(fuel)