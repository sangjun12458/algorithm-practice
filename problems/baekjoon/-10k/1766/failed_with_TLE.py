# 1766. 문제집
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

parent = tuple([] for _ in range(N+1))
child = tuple([] for _ in range(N+1))
for _ in range(M):
    A, B = map(int, input().split())
    parent[B].append(A)
    child[A].append(B)

nums = [i for i in range(1, N+1)]
answer = []
for _ in range(N):
    for x in nums:
        if not parent[x]:
            answer.append(x)
            nums.remove(x)
            for y in child[x]:
                parent[y].remove(x)
            break

print(*answer)