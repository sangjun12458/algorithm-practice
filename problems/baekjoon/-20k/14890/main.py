# 14890. 경사로
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

col_ramps = [[0, True]] * N     # length, passablity
for i in range(N):
    row_ramp = [0, True]
    for j in range(N):
        h = arr[i][j]

        if j > 0:
            row_h = arr[i][j-1]
            if h == row_h - 1:
                if row_ramp[0] < 0:
                    row_ramp[1] = False
                else:
                    row_ramp[0] = 1 - L
            elif row_h == row_h:
                row_ramp[0] += 1
            elif row_h == row_h + 1:
                if row_ramp[0] < L: 
                    row_ramp[1] = False
                else:
                    row_ramp[0] = 1
            else:
                row_ramp[1] = False
   
        if i > 0:
            col_h = arr[i-1][j]
            if h == col_h - 1:
                if col_ramps[j][0] < 0:
                    col_ramps[j][1] = False
                else:
                    col_ramps[j][0] = 1 - L
            elif h == col_h:
                col_ramps[j][0] += 1
            elif h == col_h + 1:
                if col_ramps[j][0] < L:
                    col_ramps[j][1] = False
                else:
                    col_ramps[j][0] = 1
            else:
                col_ramps[j][1] = False

    if row_ramp[0] < 0:
        passable = False

    if row_ramp[1]:
        answer += 1

for length, passablity in col_ramps:
    if length >= 0 and passablity:
        answer += 1

print(answer)