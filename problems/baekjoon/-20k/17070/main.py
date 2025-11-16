# 17070. 파이프 옮기기 1

n = int(input())
home = [input().split() for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for x in range(n):
    for y in range(n):        
        check_diagonal = True
        nx, ny = x, y + 1
        if 0 <= nx < n and 0 <= ny < n:
            if home[nx][ny] == '0':
                dp[nx][ny][0] += dp[x][y][0] + dp[x][y][2]
            else:
                check_diagonal = False
        nx, ny = x + 1, y
        if 0 <= nx < n and 0 <= ny < n:
            if home[nx][ny] == '0':
                dp[nx][ny][1] += dp[x][y][1] + dp[x][y][2]
            else:
                check_diagonal = False
        nx, ny = x + 1, y + 1
        if 0 <= nx < n and 0 <= ny < n and check_diagonal:
            if home[nx][ny] == '0':
                dp[nx][ny][2] += sum(dp[x][y])

print(sum(dp[n-1][n-1]))