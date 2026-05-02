import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    h, w = map(int, input().split())
    board = ['.' * (w+2)]
    for _ in range(h):
        board.append('.' + input().strip() + '.')
    board.append('.' * (w+2))

    h += 2
    w += 2

    keys = input().strip()
    has_key = [False] * 26

    if keys != '0':
        for k in keys:
            has_key[ord(k)-97] = True

    visited = [[False]*w for _ in range(h)]
    doors = [[] for _ in range(26)]

    q = deque([(0,0)])
    visited[0][0] = True

    answer = 0

    while q:
        y, x = q.popleft()

        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < h and 0 <= nx < w):
                continue
            if visited[ny][nx]:
                continue

            cell = board[ny][nx]

            if cell == '*':
                continue

            visited[ny][nx] = True

            # 문
            if 'A' <= cell <= 'Z':
                idx = ord(cell) - 65
                if has_key[idx]:
                    q.append((ny, nx))
                else:
                    doors[idx].append((ny, nx))

            # 열쇠
            elif 'a' <= cell <= 'z':
                idx = ord(cell) - 97
                if not has_key[idx]:
                    has_key[idx] = True
                    for door_y, door_x in doors[idx]:
                        q.append((door_y, door_x))
                q.append((ny, nx))

            # 문서
            elif cell == '$':
                answer += 1
                q.append((ny, nx))

            else:
                q.append((ny, nx))

    print(answer)
