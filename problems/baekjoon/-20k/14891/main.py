# 14891. 톱니바퀴
from collections import deque

gears = [deque(map(int, input().strip())) for _ in range(4)] # 오른쪽 2, 왼쪽 6
K = int(input())
seq = [tuple(map(int, input().split())) for _ in range(K)] # 시계 1, 반시계 -1

def turn(number, clockwise, before):
    left_cog, right_cog = gears[number][6], gears[number][2]
    if clockwise == 1:
        gears[number].appendleft(gears[number].pop())
    elif clockwise == -1:
        gears[number].append(gears[number].popleft())

    if 0 < number <= before:
        left_gear = number - 1
        if left_cog != gears[left_gear][2]:
            turn(left_gear, -clockwise, number)

    if before <= number < 3:
        right_gear = number + 1
        if right_cog != gears[right_gear][6]:
            turn(right_gear, -clockwise, number)

for n, d in seq:
    n -= 1
    turn(n, d, n)

print(sum([2**i if gears[i][0] else 0 for i in range(4)]))