# 10811. 바구니 뒤집기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
baskets = [str(x) for x in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    mid = (j - i + 1) // 2
    for k in range(mid):
        baskets[i + k], baskets[j - k] = baskets[j - k], baskets[i + k]

print(" ".join(baskets[1:]))