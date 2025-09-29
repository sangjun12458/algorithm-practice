# 11722. 가장 긴 감소하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))

dp = [0] * n
length = 0
for i in range(n):
    for j in range(i+1):
        if dp[j] <= nums[i]:
            dp[j] = nums[i]
            length = max(length, j+1)
            break
print(length)