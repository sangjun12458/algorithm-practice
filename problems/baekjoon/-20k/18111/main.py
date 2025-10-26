# 18111. 마인크래프트
import sys
input = sys.stdin.readline
FULL_STACK = 256

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
blocks = [0] * (FULL_STACK + 1)

for i in range(n):
    for j in range(m):
        blocks[land[i][j]] += 1

result_time = float('inf')
result_height = -1
for h in range(FULL_STACK + 1):
    cnt = 0
    owned_block = b
    for x in range(FULL_STACK + 1):
        d = x - h
        if d >= 0:
            cnt += 2 * d * blocks[x]
            owned_block += d * blocks[x]
        else:
            cnt -= d * blocks[x]
            owned_block += d * blocks[x]
    if owned_block < 0:
        continue
    if cnt <= result_time:
        result_time = cnt
        result_height = h

print(result_time, result_height)