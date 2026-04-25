# 15685. 드래곤 커브
DIR = [(1,0),(0,-1),(-1,0),(0,1)]

N = int(input())
grid = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())

    directions = [d]

    # 세대 커브 구현
    for _ in range(g):
        for i in range(len(directions)-1, -1, -1):
            directions.append((directions[i] + 1) % 4)

    grid[y][x] = 1
    for dir in directions:
        dx, dy = DIR[dir]
        x += dx
        y += dy
        grid[y][x] = 1
    
answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i][j+1] and grid[i+1][j] and grid[i+1][j+1]:
            answer += 1

print(answer)