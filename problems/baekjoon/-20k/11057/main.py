# 11057. 오르막 수

n = int(input().strip())
MOD = 10007

dp = [1] * 10
for _ in range(1, n):
    total = sum(dp) % MOD
    for i in range(10):
        tmp = dp[i]
        dp[i] = total
        total -= tmp
        
print(sum(dp) % MOD)