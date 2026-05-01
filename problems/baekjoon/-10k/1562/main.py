# 1562. 계단 수

import sys
input = sys.stdin.readline

MOD = 1_000_000_000
n = int(input())

# dp[length][digit][bitmask]
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]

# 초기값
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for bit in range(1 << 10):
            if dp[i-1][j][bit] == 0:
                continue

            # j-1
            if j > 0:
                nb = bit | (1 << (j-1))
                dp[i][j-1][nb] += dp[i-1][j][bit]
                dp[i][j-1][nb] %= MOD

            # j+1
            if j < 9:
                nb = bit | (1 << (j+1))
                dp[i][j+1][nb] += dp[i-1][j][bit]
                dp[i][j+1][nb] %= MOD

# 모든 숫자 사용한 경우만 합산
full = (1 << 10) - 1
answer = 0

for j in range(10):
    answer += dp[n][j][full]
    answer %= MOD

print(answer)
