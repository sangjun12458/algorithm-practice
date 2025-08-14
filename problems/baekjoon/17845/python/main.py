import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
lectures = [tuple(map(int, input().strip().split())) for _ in range(k)]
dp = [0] * (n + 1)
for importance, study_time in lectures:
    for now in range(n, study_time-1, -1):
        dp[now] = max(dp[now], dp[now-study_time] + importance)


print(dp[n])