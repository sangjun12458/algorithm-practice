# 2559. 수열
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperatures = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + temperatures[i - 1]

result = -10**9

for i in range(n - k + 1):
    result = max(result, dp[i + k] - dp[i])
    
print(result)