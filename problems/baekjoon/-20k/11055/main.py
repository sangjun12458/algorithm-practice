# 11055. 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))

dp = [0] * n
result = 0

for i in range(n):
    dp[i] = nums[i]
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])

print(max(dp))