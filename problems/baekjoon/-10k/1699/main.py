# 1699. 제곱수의 합
import math

n = int(input().strip())
m = int(math.sqrt(n))
dp = [-1] * (n + 1)
dp[0] = 0
cnt = 0

while dp[n] == -1:
    temp = []
    for i in range(n):
        if dp[i] != cnt:
            continue
        for j in range(1, m+1):
            x = i + j**2
            if x > n:
                continue
            if dp[x] > 0:
                continue
            dp[x] = cnt + 1
    cnt += 1

print(dp[n])