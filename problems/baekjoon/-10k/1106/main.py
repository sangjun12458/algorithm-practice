# 1106. 호텔
INF = 10**5

C, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]
# (비용, 인원)

cities.sort(key=lambda x: x[0] / x[1])

dp = [[INF] * (C+1) for _ in range(N)]
dp[0][0] = 0

for i in range(N):
    cost, people = cities[i]
    for j in range(C+1):
        nj = min(j + people, C)
        dp[i][nj] = min(dp[i][nj], dp[i][j] + cost)
        if i < N-1:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])

print(dp[-1][C])