# 11057. 오르막 수
import sys
input = sys.stdin.readline

n = int(input().strip())
MOD = 10007

dp = [[0] * 10 for _ in range(n + 1)]

for d in range(10):
    dp[1][d] = 1

for i in range(2, n + 1):
    for d in range(10):
        dp[i][d] = sum(dp[i-1][:d+1]) % MOD

print(sum(dp[n]) % MOD)
