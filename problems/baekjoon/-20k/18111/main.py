# 18111. 마인크래프트
import sys
input = sys.stdin.readline
FULL_STACK = 256

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

result = float('inf')
height = -1
for h in range(FULL_STACK + 1):
    cnt = 0
    blocks = b
    for i in range(n):
        for j in range(m):
            d = land[i][j] - h

            if d >= 0:
                cnt += d * 2
                blocks += d
            else:
                cnt -= d
                blocks += d

    if blocks < 0:
        continue
    
    if cnt <= result:
        result = cnt
        height = h

print(result, height)