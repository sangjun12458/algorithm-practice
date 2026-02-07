# 14499. 주사위 굴리기

N, M, x, y, K = map(int, input().split())
map_for_dice = []
for _ in range(N):
    map_for_dice.append(list(map(int, input().split())))
dirs = list(map(int, input().split())) # 동 1, 서 2, 북 3, 남 4
delta = ((0, 0), (0, 1), (0, -1), (-1, 0), (1, 0))
dice = [0] * 7
#   2
# 4 1 3
#   5
#   6

for dir in dirs:
    dx, dy = delta[dir]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    if dir == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif dir == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif dir == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif dir == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

    if map_for_dice[nx][ny] == 0:
        map_for_dice[nx][ny] = dice[1]
    else:
        dice[1] = map_for_dice[nx][ny]
        map_for_dice[nx][ny] = 0        
    x, y = nx, ny
    print(dice[6])