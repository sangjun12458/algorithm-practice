from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    command = input().strip()
    if command.startswith('push'):
        _, num = command.split()
        q.append(int(num))
    elif command == "pop":
        print(q.popleft() if q else -1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        print(0 if q else 1)
    elif command == "front":
        print(q[0] if q else -1)
    elif command == "back":
        print(q[-1] if q else -1)