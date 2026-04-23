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
        er, ec = curves[-1]
        l = len(curves)
        for i in range(l-2, -1, -1):
            pr, pc = curves[i]
            # 기준점에 대해 회전
            dr, dc = er - ec, er + ec
            nr, nc = pc + dr, -pr + dc
            if 0 <= nr <= 100 and 0 <= nc <= 100:
                curves.append((nr, nc))
            # else:
            #     break
            
    for y, x in curves:
        grid[y][x] = 1
    
answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1] == 1:
            answer += 1
print(answer)