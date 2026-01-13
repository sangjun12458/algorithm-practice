# 1005. ACM Craft
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    seq = [[] for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        seq[X].append(Y)
    W = int(input())

    start = [True] * (N+1) 
    start[0] = False
    for A, Bs in enumerate(seq):
        for B in Bs:
            start[B] = False

    q = deque()
    total_time = [0] * (N+1)
    for num, canStart in enumerate(start):
        if canStart:
            q.append(num)
            total_time[num] = time[num]

    while q:
        now = q.popleft()
        for new in seq[now]:
            total_time[new] = max(total_time[new], total_time[now] + time[new])
            q.append(new)
        
    print(total_time[W])