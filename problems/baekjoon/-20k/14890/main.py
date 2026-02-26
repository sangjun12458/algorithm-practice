# 14890. 경사로
from collections import deque

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(N):
    ramp = deque()
    passable = True
    for j in range(N):            
        if not ramp:
            ramp.append(j)
            continue
        h = arr[i][ramp[0]]
        nh = arr[i][j]

        if nh == h + 1:
            if len(ramp) == L:
                ramp.clear()
                ramp.append(j)
            else:
                passable = False
                break
        elif nh == h:
            ramp.append(j)
            if len(ramp) > L:
                ramp.popleft()
        elif nh == h - 1:
            ramp.clear()
            ramp.append(j)
        else:
            passable = False
            break

    if passable:
        print(arr[i])
        answer += 1

print(answer)