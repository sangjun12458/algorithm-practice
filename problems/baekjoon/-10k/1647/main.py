# 1647. 도시 분할 계획
import sys
input = sys.stdin.readline
INF = 10**8

def find_root(x):
    if roots[x] == x:
        return x
    else:
        return find_root(roots[x])

def union(u, v):
    r1 = find_root(u)
    r2 = find_root(v)    
    if r1 == r2:
        return False
    else:
        if r1 < r2:
            roots[r2] = r1
        else:
            roots[r1] = r2
        return True

N, M = map(int, input().split())
roads = []
for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((C, A, B))
roads.sort(reverse=True)

total_cost = 0
town_count = N
roots = [i for i in range(N+1)]

while roads and town_count > 2:
    cost, a, b = roads.pop()
    if union(a, b):
        town_count -= 1
        total_cost += cost

print(total_cost)