# 2629. 양팔저울
import sys
input = sys.stdin.readline

num_weights = int(input().strip())
weights = list(map(int, input().split()))
num_beads = int(input().strip())
beads = list(map(int, input().split()))

total = sum(weights)
dp = [[False] * (2 * total + 1) for _ in range(num_weights + 1)]
dp[0][total] = True

for i in range(num_weights):
    w = weights[i]
    for j in range(2 * total + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
            if j - w >= 0:
                dp[i + 1][j - w] = True
            if j + w <= 2 * total:
                dp[i + 1][j + w] = True

for bead in beads:
    if 0 <= bead + total <= 2 * total:
        if dp[num_weights][bead + total]:
            print("Y")
        else:
            print("N")
    else:
        print("N")