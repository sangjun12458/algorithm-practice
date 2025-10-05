# 2133. 타일 채우기
n = int(input().strip())
dp = [0] * (n+1)
dp[0] = 1
cum = 1
for i in range(2, n+1, 2):
    dp[i] = dp[i-2] + cum * 2
    cum += dp[i]
print(dp[n])