# 15685. 드래곤 커브
DIR = ((0, 1), (-1, 0), (0, -1), (1, 0))

N = int(input())
grid = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    dy, dx = DIR[d]
    curves = [(y, x), (y + dy, x + dx)]

    # 세대 커브 구현
    for _ in range(g):
        l = len(curves)
        oy, ox = curves[-1]
        for i in range(l):
            py, px = curves[i]
            # 기준점에 대해 회전
            curves.append((py, px))

    for y, x in curves:
        grid[y][x] = 1
    
    for row in grid[:10]:
        print(row[:10])
    print()

answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1]:
            answer += 1
print(answer)