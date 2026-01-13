# 1005. ACM Craft
import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    phase = [0] * (N+1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        phase[Y] += 1
    W = int(input())

    heap = []
    total = [0] * (N+1)
    for i in range(1, N+1):
        if phase[i] == 0:
            heapq.heappush(heap, i)
    while heap:
        now = heapq.heappop(heap)
        total[now] += time[now]
        if now == W:
            break
        for new in graph[now]:
            phase[new] -= 1
            if phase[new] == 0:
                heapq.heappush(heap, new)
            total[new] = max(total[new], total[now])

    print(total[W])