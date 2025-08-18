import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
q = deque([(a, 1)])

while q:
    x, depth = q.popleft()
    if x == b:
        print(depth)
        break
    if x * 2 <= b:
        q.append((x * 2, depth + 1))
    if x * 10 + 1 <= b:
        q.append((x * 10 + 1, depth + 1))
else:
    print(-1)