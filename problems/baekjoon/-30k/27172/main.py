# 27172. 수 나누기 게임
import math
MAX_NUM = 1_000_000

N = int(input())
card_of_player = list(map(int, input().split()))
player_of_card = [-1] * (MAX_NUM + 1)
scores = [0] * N

max_value = 0
for i in range(N):
    player_of_card[card_of_player[i]] = i
    max_value = max(max_value, card_of_player[i])

for num in card_of_player:
    for k in range(num*2, max_value+1, num):
        if player_of_card[k] == -1: continue
        if k % num != 0: continue
        scores[player_of_card[num]] +=1 
        scores[player_of_card[k]] -= 1

print(*scores)