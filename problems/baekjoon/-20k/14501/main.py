# 14501. 퇴사
import sys
input = sys.stdin.readline

n = int(input().strip())
counsels = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 2)
for i in range(n):
    t, p = counsels[i]
    start = i + 1
    end = start + t
    if end <= n + 1:
        dp[end] = max(dp[end], dp[start] + p)
    dp[start + 1] = max(dp[start + 1], dp[start])

print(dp[n+1])