# 2342. Dance Dance Revolution
INF = 10**6
# POS = {(1, 2): 0, (1, 3): 1, (1, 4): 2,
#        (2, 1): 0, (2, 3): 3, (2, 4): 4,
#        (3, 1): 1, (3, 2): 3, (3, 4): 5,
#        (4, 1): 2, (4, 2): 4, (4, 3): 5}

POS = [[-1] * 5 for _ in range(5)]
cnt = 0
for i in range(4):
    for j in range(i+1, 5):
        if i == j: continue
        POS[i][j] = POS[j][i] = cnt
        cnt += 1

seq = list(map(int, input().split()))

ans = INF
stack = [(0, 0, 0, 0)]
while stack and False:
    left, right, depth, cost = stack.pop()
    now = seq[depth]
    #print(left, right, now,cost)
    if now == 0:
        ans = min(ans, cost)
        continue
    if cost + len(seq) - depth > ans:
        continue
    
    if left == 0:
        stack.append((now, right, depth+1, cost+2))
    elif left == now or right == now:
        stack.append((left, right, depth+1, cost+1))
    else:
        if (left + 1) % 4 + 1 == now:
            stack.append((now, right, depth+1, cost+4))
        else:
            stack.append((now, right, depth+1, cost+3))
        
        if right == 0:
            stack.append((left, now, depth+1, cost+2))
        elif (right + 1) % 4 + 1 == now:
            stack.append((left, now, depth+1, cost+4))
        else:
            stack.append((left, now, depth+1, cost+3))

dp = [[INF] * 10 for _ in range(len(seq))]
dp[0][POS[0][seq[0]]] = 2
for idx, num in enumerate(seq):
    if idx * num == 0: continue

    for x in range(9):
        for y in range(x+1, 10):
            if x == num or y == num:
                now = POS[x][y]
                dp[idx+1][now] = min(dp[idx+1][now], dp[idx][now] + 1)
            else:
                if y == 0:
                    now = POS[x][y]
                    new = POS[x][y]

    for x in range(1, 4):
        for y in range(x+1, 5):
            if x == num or y == num:
                now = POS[(x, y)]
                dp[idx][now] = min(dp[idx][now], dp[idx-1][now] + 1)
            else:
                now = POS[(x, y)]
                new = POS[(x, num)]
                if (y+1)%4+1 == num:
                    dp[idx][new] = min(dp[idx][new], dp[idx-1][now] + 4)
                else:
                    dp[idx][new] = min(dp[idx][new], dp[idx-1][now] + 3)
                new = POS[(num, y)]
                if (x+1)%4+1 == num:
                    dp[idx][new] = min(dp[idx][new], dp[idx-1][now] + 4)
                else:
                    dp[idx][new] = min(dp[idx][new], dp[idx-1][now] + 3)

# for row in dp:
#     print(*row)
print(min(dp[-2]))