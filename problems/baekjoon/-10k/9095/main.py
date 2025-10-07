# 9095. 1, 2, 3 더하기
END = 11
dp = [0] * (END+1)
dp[1] = 1
dp[2] = dp[1] + 1
dp[3] = dp[2] + dp[1] + 1

t = int(input().strip())
for i in range(4, END+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input().strip())
    print(dp[n])