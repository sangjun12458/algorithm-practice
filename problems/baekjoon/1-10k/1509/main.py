# 1509. 팰린드롬 분할
import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)
dp_pal = [[False] * n for _ in range(n)]

for i in range(n):
    dp_pal[i][i] = True

for i in range(n-1):
    if s[i] == s[i+1]:
        dp_pal[i][i+1] = True

for length in range(3, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        if s[i] == s[j] and dp_pal[i+1][j-1]:
            dp_pal[i][j] = True

dp = [float('inf')] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    for j in range(i):
        if dp_pal[j][i-1]:
            dp[i] = min(dp[i], dp[j] + 1)

print(dp[n])