# 1865. 웜홀
import sys
input = sys.stdin.readline
INF = int(1e6)

tc = int(input().strip())

def solve():
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    dist = [INF] * (n+1)
    dist[1] = 0
    for _ in range(n-1):
        for s, e, t in edges:
            dist[e] = min(dist[e], dist[s] + t)

    for s, e, t in edges:
        if dist[s] + t < dist[e]:
                return True
    return False

for _ in range(tc):
    if solve():
        print("YES")
    else:
        print("NO")