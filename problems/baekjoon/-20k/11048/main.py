# 11048. 이동하기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m+1) for _ in range(n+1)]
cnt = dp[0][0]

for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = max(max(dp[i][j+1], dp[i+1][j]), dp[i][j]) + candies[i][j]

print(dp[n][m])