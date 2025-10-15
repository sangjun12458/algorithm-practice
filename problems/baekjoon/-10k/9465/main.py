# 9465. 스티커
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(3)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + stickers[1][i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1])
        
    print(max(dp[0][n-1], dp[1][n-1]))