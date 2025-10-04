# 2133. 타일 채우기
n = int(input().strip())
dp = [0] * (n+1)
if n >= 2:
    dp[2] = 3
for i in range(4, n+1):
    dp[i] = dp[i-2] * 3 + dp[i-1]
print(dp[n])