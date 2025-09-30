# 2294. 동전 2
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = [int(input().strip()) for _ in range(n)]
coin_set = set(coin_list)

dp = [0] + [k + 1] * (k)
for i in range(1, k+1):
    for coin in coin_set:
        x = i - coin
        if x < 0: continue
        dp[i] = min(dp[i], dp[x] + 1)

if dp[k] == k + 1:
    print(-1)
else:
    print(dp[k])