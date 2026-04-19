# 19238. 스타트 택시
from collections import deque
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MAX_D = 1000

N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ty, tx = map(lambda x: int(x)-1, input().split())

passengers = {}
for _ in range(M):
    sy, sx, ey, ex = map(lambda x: int(x)-1, input().split())
    passengers[(sy, sx)] = (ey, ex)

for _ in range(M):
    # 택시로부터 최단거리 승객 찾기
    visited = [[-1] * N for _ in range(N)]
    q = deque([(ty, tx)])
    visited[ty][tx] = 0
    target = None
    while q:
        y, x = q.popleft()
        if passengers.get((y, x)):
            if visited[y][x] > visited[target[0]][target[1]]:
                break
            if target is None:
                target = (y, x)

            if target[0] < y:
                target = (y, x)
            elif target[0] == y and target[1] < x:
                target = (y, x)

        for dy, dx in DIR:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if arr[ny][nx]:
                continue
            if visited[ny][nx] != -1:
                continue
            q.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1
    if target is None: # 승객에게 갈 수 없으므로 종료
        fuel = -1
        break
    print(fuel)
    fuel -= visited[target[0]][target[1]]
    print(fuel)

    # 출발지에서 목적지까지 최단거리
    ey, ex = passengers[target]
    passengers.pop(target)
    visited = [[-1] * N for _ in range(N)]
    q = deque([target])
    visited[target[0]][target[1]] = 0
    fuel_used = float('inf')
    while q:
        y, x = q.popleft()
        if y == ey and x == ex:
            print(y, x)
            fuel_used = visited[y][x]
            break
        for dy, dx in DIR:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if arr[ny][nx]:
                continue
            if visited[ny][nx] != -1:
                continue
            q.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1

    if fuel_used > fuel: # 길이 없거나 연료가 부족하여 종료
        fuel = -1
        break
    fuel += fuel_used
    ty, tx = ey, ex

    print(fuel)
    print()

print(fuel)