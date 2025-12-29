# 2342. Dance Dance Revolution
INF = 10**6
POS = [[-1] * 5 for _ in range(5)]
cnt = 0
for i in range(4):
    for j in range(i+1, 5):
        if i == j: continue
        POS[i][j] = POS[j][i] = cnt
        cnt += 1

seq = list(map(int, input().split()))

dp = [[INF] * 10 for _ in range(len(seq)-1)]
dp[0][POS[0][seq[0]]] = 2
for idx, num in enumerate(seq):
    if idx * num == 0: continue

    for x in range(4):
        for y in range(x+1, 5):
            if x == num or y == num:
                now = POS[x][y]
                dp[idx][now] = min(dp[idx][now], dp[idx-1][now] + 1)
            else:
                now = POS[x][y]
                new = POS[num][y]
                if x == 0:
                    cost = 2
                elif (x+1)%4+1 == num:
                    cost = 4
                else:
                    cost = 3
                dp[idx][new] = min(dp[idx][new], dp[idx-1][now] + cost)

                new = POS[x][num]
                if y == 0:
                    cost = 2
                elif (y+1)%4+1 == num:
                    cost = 4
                else:
                    cost = 3
                dp[idx][new] = min(dp[idx][new], dp[idx-1][now] + cost)

print(min(dp[-1]))