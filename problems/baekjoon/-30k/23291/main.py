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
    grid[-1] = fishes
    h, w = 1, 1
    r_start = N - 1
    c_start = 0
    while c_start+h+w < N:
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
    
    for r in range(N):
        for c in range(N):
            if grid[r][c] > 0:


def serialize():
    idx = -1
    for c in range(N-1, -1, -1):
        for r in range(N-1, -1, -1):
            if grid[r][c] > 0:
                idx += 1
                fishes[idx] = grid[r][c]

def process_2():
    return

while ans < 1:
    # if check():
    #     print(ans)
    #     break
    add()
    process_1()
    control()
    serialize()
    process_2()
    control()
    serialize()
    ans += 1