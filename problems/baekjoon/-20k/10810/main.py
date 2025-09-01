# 10810. 공 넣기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
baskets = ["0"] * (n+1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for index in range(i, j+1):
        baskets[index] = str(k)

print(" ".join(baskets[1:]))