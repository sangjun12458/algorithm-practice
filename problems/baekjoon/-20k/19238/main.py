# 19238. 스타트 택시
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, gas = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(int, input().split()))
customer = [list(map(int, input().split())) + [False] for _ in range(M)]

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
        r, c, _, _, proccessed = customer[i]
        if proccessed:
            continue
        d = dist[taxi[0]*N+taxi[1]][r*N+c]
        if d < best_d:
            best_d = d
            target = i
    
    # 출발지에서 목적지까지 최단거리 + 가지 못하거나 연료가 없으면 종료
    # 연료 충전 
    pass

