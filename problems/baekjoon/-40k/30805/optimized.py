# 30805. 사전 순 최대 공통 부분 수열
MAX_NUM = 100

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

apos = [[] for _ in range(MAX_NUM+1)]
bpos = [[] for _ in range(MAX_NUM+1)]

for idx, x in enumerate(A):
    apos[x].append(idx)

for idx, x in enumerate(B):
    bpos[x].append(idx)

ai = bi = -1
ans = []

for i in range(MAX_NUM, 0, -1):
    ai_pos = []
    for j in apos[i]:
        if j > ai:
            ai_pos.append(j)
    if not ai_pos:
        continue

    bi_pos = []
    for j in bpos[i]:
        if j > bi:
            bi_pos.append(j)
    if not bi_pos:
        continue

    pair_len = min(len(ai_pos), len(bi_pos))
    ans.extend([i] * pair_len)
    ai, bi = ai_pos[pair_len-1], bi_pos[pair_len-1]

print(len(ans))
print(*ans)