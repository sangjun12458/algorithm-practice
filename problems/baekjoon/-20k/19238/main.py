# 19238. 스타트 택시
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, gas = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
taxi_r, taxi_c = map(lambda x: int(x)-1, input().split())
customer = [list(map(lambda x: int(x)-1, input().split()))]
proccessed = [False] * N

dist = [[-1] * (N*N) for _ in range(N*N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            continue
        start = i * N + j
        q = [(i, j, 0)]
        while q:
            r, c, d = q.pop()
            if not (0 <= r < N and 0 <= c < N):
                continue
            if arr[r][c] == 1:
                continue
            end = r * N + c
            if dist[start][end] != -1:
                continue
            dist[start][end] = dist[end][start] = d
            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                q.append((nr, nc, d + 1))

for _ in range(M):
    # 택시로부터 최단거리 승객 찾기 + 찾을 수 없으면 종료
    target, best_d = -1, 1000
    for i in range(M):
        if proccessed[i]:
            continue
        customer_r, customer_c, _, _ = customer[i]
        visited = [[False] * N for _ in range(N)]
        q = [(taxi_r, taxi_c, 0)]
        while q:
            r, c, d = q.pop()
            if r == customer_r and c == customer_c:
                if d < best_d:
                    best_d = d
                    target = i
            if visited[r][c]:
                continue
            visited[r][c] = True
            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    q.append((nr, nc, d + 1))

    if target == -1:
        gas = -1
        break
    # 출발지에서 목적지까지 최단거리 + 가지 못하거나 연료가 없으면 종료
    sr, sc, er, ec = customer[target]
    v = visited[target]
    gas -= best_d
    gas_used = dist[sr*N+sc][er*N+ec]
    if gas < gas_used:
        gas = -1
        break
    gas += gas_used
    taxi = [er, ec]
    customer[target][4] = True

print(gas)