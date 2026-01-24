# 20303. 할로윈의 양아치
import sys
input = sys.stdin.readline

def find_parent(x):
    return x if x == parent[x] else find_parent(parent[x])

def union(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))
parent = [0] + [i for i in range(1, N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

group = dict()
for i in range(1, N+1):
    p = find_parent(i)
    if group.get(p):
        group[p] = (group[p][0]+1, group[p][1]+candy[i])
    else:
        group[p] = (1, candy[i])

dp = [0] * (K)
for key, (num_people, num_candy) in group.items():
    for i in range(K-1, num_people-1, -1):
        dp[i] = max(dp[i], dp[i-num_people] + num_candy)

print(max(dp))