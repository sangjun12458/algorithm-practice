# 14890. 경사로
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(N):
    ramp_h = arr[i][0]
    ramp_l = 1
    passable = True
    for j in range(1, N):
        h = arr[i][j]
        if h + 1 == ramp_h:
            if ramp_l >= 0:
                ramp_h = h
                ramp_l = 1 - L
            else:
                passable = False
                break
        elif h == ramp_h:
            ramp_l += 1
        elif h - 1 == ramp_h:
            if ramp_l >= L:
                ramp_l = 1
                ramp_h = h
            else:
                passable = False
                break
        else:
            passable = False
            break
    if ramp_l < 0:
        passable = False

    if passable:
        # print(arr[i])
        answer += 1

for j in range(N):
    ramp_h = arr[0][j]
    ramp_l = 1
    passable = True
    for i in range(1, N):
        h = arr[i][j]
        if h + 1 == ramp_h:
            if ramp_l >= 0:
                ramp_h = h
                ramp_l = 1 - L
            else:
                passable = False
                break
        elif h == ramp_h:
            ramp_l += 1
        elif h - 1 == ramp_h:
            if ramp_l >= L:
                ramp_l = 1
                ramp_h = h
            else:
                passable = False
                break
        else:
            passable = False
            break
    if ramp_l < 0:
        passable = False

    if passable:
        # print()
        # for row in arr:
        #     print(row[j])
        answer += 1

print(answer)