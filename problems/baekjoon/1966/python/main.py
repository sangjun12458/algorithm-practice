import sys
sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    q = deque()
    
    n, m = input().strip().split()
    n, m = int(n), int(m)
    prior = input().strip().split()
    for i in range(n):
        q.append(prior[i])
    
    
    result = 0
    while q and (m >= 0):
        result += 1
        max = q[0]
        for i in range(len(q)):
            if q[i] > max:
                max = q[i]
        while q[0] != max:
            q.rotate(-1)
            m = (len(q) + m - 1) % len(q)
        if m == 0:
            m = -1
        else:
            temp = q.popleft()
            m = (len(q) + m - 1) % len(q)

    print(result)
    
        