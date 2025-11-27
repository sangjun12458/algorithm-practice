# 12851. 숨바꼭질 2
from collections import deque
MAX_NUM = 10**5

N, K = map(int, input().split())
time = [-1] * (MAX_NUM + 1)
time[K] = 0
q = deque([K])

answer = 0
while q and time[N] == -1:
    x = q.popleft()
    # if x == N:
    #     if time[N] != -1:
            
            
    # else:

    for k in [-1, 1]:
        y = x + k
        if 0 <= y <= MAX_NUM and time[y] == -1:
            time[y] = time[x] + 1
            q.append(y)
    if x % 2 == 0:
        y = x // 2
        if 0 <= y <= MAX_NUM and time[y] == -1:
            time[y] = time[x] + 1
            q.append(y)


print(time[N])