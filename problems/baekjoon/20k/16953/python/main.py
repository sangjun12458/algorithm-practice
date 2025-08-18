import sys
input = sys.stdin.readline
from collections import deque

ab = input().strip().split()
a = int(ab[0])
b = int(ab[1])
q = deque()

q.append([a, 1])

result = -1

while q:
    x, depth = q.popleft()
    if x == b:
        result = depth
        break
    elif x < b:
        q.append([x * 2, depth+1])
        q.append([10 * x + 1, depth+1])

print(result)