# 19238. 스타트 택시
from collections import deque
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, gas = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
taxi_r, taxi_c = map(lambda x: int(x)-1, input().split())
customer = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]

proccessed = [False] * N
for _ in range(M):
    # 택시로부터 최단거리 승객 찾기 + 찾을 수 없으면 종료
    target, best_d = -1, 1000
    for i in range(M):
        if proccessed[i]:
            continue
        customer_r, customer_c, _, _ = customer[i]
        visited = [[False] * N for _ in range(N)]
        q = deque([(taxi_r, taxi_c, 0)])
        while q:
            r, c, d = q.popleft()
            if r == customer_r and c == customer_c:
                if d < best_d:
                    best_d = d
                    target = i
                break
            if visited[r][c]:
                continue
            visited[r][c] = True
            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if arr[r][c]:
                    continue
                q.append((nr, nc, d + 1))
    if target == -1:
        gas = -1
        break
    gas -= best_d
    # 출발지에서 목적지까지 최단거리 + 가지 못하거나 연료가 없으면 종료
    sr, sc, er, ec = customer[target]
    visited = [[False] * N for _ in range(N)]
    q = deque([(sr, sc, 0)])
    gas_used = -1
    while q:
        r, c, d = q.popleft()
        if r == er and c == ec:
            gas_used = d
            break
        if visited[r][c]:
            continue
        visited[r][c] = True
        for dr, dc in DIR:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                q.append((nr, nc, d + 1))

    if gas_used == -1 or gas_used > gas:
        gas = -1
        break

    gas += gas_used
    taxi_r, taxi_c = er, ec
    proccessed[target] = True

print(gas)