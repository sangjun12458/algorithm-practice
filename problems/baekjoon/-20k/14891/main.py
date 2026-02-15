# 14891. 톱니바퀴
from collections import deque
gears = [deque(input().strip()) for _ in range(4)] # 오른쪽 2, 왼쪽 6
K = int(input())
seq = [tuple(map(int, input().split())) for _ in range(K)] # 시계 1, 반시계 -1

def turn(number, clockwise):
    if clockwise == 1:
        gears[number].appendleft(gears[number].pop())
    else:
        gears[number].append(gears[number].popleft())

for n, d in seq:
    left, right = gears[n][6], gears[n][2]
    turn(n, d)
    