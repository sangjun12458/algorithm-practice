# 15686. 치킨 배달
from collections import deque
MAX_NUM = int(10e9)

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

dist = [[0] * (len(chicken)) for _ in range(len(house))]

for i in range(len(house)):
    hx, hy = house[i]
    for j in range(len(chicken)):
        cx, cy = chicken[j]
        dist[i][j] = abs(hx - cx) + abs(hy - cy)

result = MAX_NUM
q = deque()
q.append([])
while q:
    opened = q.popleft()
    if len(opened) == m:
        total_d = 0
        for i in range(len(house)):
            one_d = MAX_NUM
            for j in opened:
                one_d = min(one_d, dist[i][j])
            total_d += one_d
        result = min(result, total_d)
    elif len(opened) < m:
        for i in range(len(chicken)):
            if opened and opened[-1] <= i:
                continue
            q.append(opened[:] + [i])

print(result)