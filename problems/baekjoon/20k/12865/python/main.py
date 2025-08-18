import sys

input = sys.stdin.readline

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(k + 1)] for _ in range(n)]

if items[0][0] <= k:
    dp[0][items[0][0]] = items[0][1]

for i in range(1, n):
    w, v = items[i][0], items[i][1]
    for j in range(1, k + 1):
        if j - w < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(max(dp[n-1]))
