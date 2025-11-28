# 12851. 숨바꼭질 2
from collections import deque
MAX_NUM = 10**5

def step(y):
    global answer
    if 0 <= y <= MAX_NUM and time[x] + 1 <= time[y]:
        if y == N:
            time[N] = time[x] + 1
            if time[x] + 1 < time[N]:
                answer = 1
            else:
                answer += 1
        else:
            if time[x] + 1 < time[N]:
                time[y] = time[x] + 1
                q.append(y)

N, K = map(int, input().split())
time = [MAX_NUM] * (MAX_NUM + 1)
time[K] = 0
q = deque([K])

answer = 0
while q:
    x = q.popleft()
    step(x - 1)
    step(x + 1)
    if x % 2 == 0:
        step(x // 2)

print(time[N])
if N == K:
    print(1)
else:
    print(answer)