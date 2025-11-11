# 16928. 뱀과 사다리 게임
from collections import deque
q = deque()
board = [0] * 101
rolls = [-1] * 101

n, m = map(int, input().split())
for _ in range(n + m):
    a, b = map(int, input().split())
    board[a] = b

q.append(1)
rolls[1] = 0
while q:
    start = q.popleft()
    for i in range(1, 7):
        end = start + i
        if end > 100: continue
        end = board[end] if board[end] else end
        if rolls[end] != -1: continue
        rolls[end] = rolls[start] + 1
        q.append(end)

print(rolls[100])