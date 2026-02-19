# 13975. 파일 합치기 3
import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    chapters = list(map(int, input().split()))
    groups = [i for i in range(k)]
    result = 0
    for _ in range(k-1):
        costs = []
        for i in range(k-1):
            left, pl, gl = i, chapters[i], groups[i]
            right, pr, gr = i+1, chapters[i+1], groups[i+1]
            if gl == gr: continue
            costs.append((pl + pr, gl, gr))
        costs.sort()

        cost, gl, gr = costs[0]
        result += cost
        for i in range(k):
            if groups[i] in [gl, gr]:
                chapters[i] = cost
                groups[i] = gl

        print(chapters)
        
    print(result)