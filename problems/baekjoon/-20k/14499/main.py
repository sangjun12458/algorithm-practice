# 14499. 주사위 굴리기

N, M, x, y, K = map(int, input().split())
map_for_dice = []
for _ in range(N):
    map_for_dice.append(list(map(int, input().split())))
seq = list(map(int, input().split()))

print(map_for_dice)
