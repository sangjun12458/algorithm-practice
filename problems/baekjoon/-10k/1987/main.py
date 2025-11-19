# 1987. 알파벳
from collections import deque
DIR = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def str_to_num(x : str):
    return ord(x) - ord('A')

r, c = map(int, input().split())
board = [list(map(str_to_num, input())) for _ in range(r)]

s = set()
for i in range(r):
    for j in range(c):
        s.add(board[i][j])
max_num = len(s)

result = 1
q = deque([(0, 0, 1 << board[0][0])])
while q:
    y, x, value = q.popleft()

    for dy, dx in DIR:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < r and 0 <= nx < c):
            continue
        nv = 1 << board[ny][nx]
        if value & nv != 0:
            cnt = 0
            for i in range(26):
                if value & 1 << i != 0:
                    cnt += 1
            result = max(result, cnt)
        else:
            q.append((ny, nx, value | nv))

print(result)