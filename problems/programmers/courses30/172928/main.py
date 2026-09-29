# 공원 산책

def solution(park, routes):
    answer = []
    H, W = len(park), len(park[0])
    dyx = {'N': (-1, 0), 'E': (0, 1), 'W': (0, -1), 'S': (1, 0)}

    y, x = None, None
    for i in range(H):
        if y and x:
            break
        for j in range(W):
            if park[i][j] == 'S':
                y, x = i, j
                break

    for route in routes:
        dir, dist = route.split()
        dist = int(dist)
        dy, dx = dyx[dir]
        ny = y + dy * dist
        nx = x + dx * dist
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        is_blocked = False
        if dy != 0:
            for i in range(y+dy, ny+dy, dy):
                if park[i][x] == 'X':
                    is_blocked = True
                    break
        elif dx != 0:
            for j in range(x+dx, nx+dx, dx):
                if park[y][j] == 'X':
                    is_blocked = True
                    break
        if is_blocked:
            continue
        y, x = ny, nx

    answer = y, x
    return answer