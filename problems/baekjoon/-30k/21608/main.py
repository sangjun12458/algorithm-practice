# 21608. 상어 초등학교
import sys
input = sys.stdin.readline

N = int(input())
preferred = [0] * N * N
for _ in range(N*N):
    x, y1, y2, y3, y4 = map(int, input().split())
    preferred[x-1] = (y1, y2, y3, y4)

print(preferred)