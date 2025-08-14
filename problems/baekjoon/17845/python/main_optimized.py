import sys

n, k, *data = map(int, sys.stdin.read().split())
dp = [0] * (n + 1)

for importance, study_time in zip(data[::2], data[1::2]):
    for now in range(n, study_time - 1, -1):
        dp[now] = max(dp[now], dp[now - study_time] + importance)

print(dp[n])