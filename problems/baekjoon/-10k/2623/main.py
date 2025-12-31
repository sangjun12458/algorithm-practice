# 2623. 음악프로그램
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = [list(map(int, input().split())) for _ in range(M)]

unlinked = [i for i in range(1, N+1)]
linked = []

front = [[] for _ in range(N+1)]
back = [[] for _ in range(N+1)]

for s in seq:
    for i in range(len(s)-2):
        a = s[i+1]
        b = s[i+2]
        front[b].append(a)
        back[a].append(b)

answer = []
for _ in range(N):
    for x in unlinked:
        if front[x]:
            continue
        
        unlinked.remove(x)
        linked.append(x)
        answer.append(x)
        for y in back[x]:
            front[y].remove(x)

        break

if len(answer) != N:
    print(0)
else:
    print("\n".join(map(str, answer)))