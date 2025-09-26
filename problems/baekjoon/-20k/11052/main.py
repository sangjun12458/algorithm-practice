# 11052. 카드 구매하기
import sys
input = sys.stdin.readline

n = int(input().strip())
packs = [0] + list(map(int, input().split()))  # 1-based index
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + packs[j])

print(dp[n])