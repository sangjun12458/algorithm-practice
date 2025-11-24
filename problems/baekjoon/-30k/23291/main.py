# 23291. 어항 정리

N, K = map(int, input().split())
fishes = list(map(int, input().split()))
ans = 0
grid = [[0]*N for _ in range(N)]

def check():
    return max(fishes) - min(fishes) <= K

def add():
    min_v = min(fishes)
    for i in range(N):
        if fishes[i] == min_v:
            fishes[i] += 1

def print_grid():
    for row in grid:
        print(row)
    print()

def process_1():
    for i in range(len(fishes)):
        grid[-1][i] = fishes[i]
    h, w = 1, 1
    r_start = N - 1
    c_start = 0
    while c_start+h+w-1 < N:
        # 영역 선택
        target = []
        for i in range(r_start, r_start - h, -1):
            for j in range(c_start, c_start + w):
                target.append((i, j))

        # translation + rotation + translation
        oy, ox = target[0][0], target[0][1]
        for i in range(len(target)):
            y, x = target[i][0], target[i][1]
            ny = y - oy
            nx = x - ox
            ny, nx = oy + nx - w, ox - ny + w
            grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]
        c_start += w
        h, w = w + 1, h

def control():
    d_fish = []
    for y in range(N):
        for x in range(N):
            if grid[y][x] > 0:
                diff = 0
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < N and 0 <= nx < N):
                        continue
                    if grid[ny][nx] == 0:
                        continue
                    share = abs(grid[y][x] - grid[ny][nx]) // 5
                    diff += share if grid[y][x] < grid[ny][nx] else -share
                d_fish.append((y, x, diff))

    for y, x, d in d_fish:
        grid[y][x] += d

def serialize():
    idx = -1
    for c in range(N):
        for r in range(N-1, -1, -1):
            if grid[r][c] > 0:
                idx += 1
                fishes[idx] = grid[r][c]
                grid[r][c] = 0

def process_2():
    for i in range(len(fishes)):
        grid[-1][i] = fishes[i]
    
    floating = []
    for x in range(N//2):
        floating.append((N-1, x))

    oy, ox = floating[0]
    dy, dx = -1, N-1
    for y, x in floating:
        ny, nx = 2*oy-y+dy, 2*ox-x+dx
        grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]

    floating.clear()
    for y in [N-1, N-2]:
        for x in range(N//2, 3*N//4):
            floating.append((y, x))

    oy, ox = floating[0]
    dy, dx = -3, N//2-1
    for y, x in floating:
        ny, nx = 2*oy-y+dy, 2*ox-x+dx
        grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]

while not check():
    add()
    process_1()
    control()
    serialize()
    process_2()
    control()
    serialize()
    ans += 1

print(ans)