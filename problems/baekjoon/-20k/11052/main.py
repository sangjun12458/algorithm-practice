# 11052. 카드 구매하기
import sys
input = sys.stdin.readline

n = int(input().strip())
packs = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n+1):
    for j in range(0, i):
        dp[i] = max(dp[i], dp[i-j-1] + packs[j])

print(dp[n])