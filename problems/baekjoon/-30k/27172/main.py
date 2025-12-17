# 27172. 수 나누기 게임
import math
MAX_NUM = 1_000_000

N = int(input())
players = list(map(int, input().split()))
cards = [-1] * (MAX_NUM + 1)
scores = [0] * N

for i in range(N):
    cards[players[i]] = i

for i in range(1, 1001):
    for j in range(i*i, MAX_NUM+1):
        #print(i, j)

        if j % i != 0 or cards[j] == -1:
            continue
        if cards[i] != -1:
            scores[cards[i]] += 1
            scores[cards[j]] -= 1

        if i * i == j:
            continue

        if cards[j // i] != -1:
            scores[cards[j // i]] += 1
            scores[cards[j]] -= 1

print(*scores)