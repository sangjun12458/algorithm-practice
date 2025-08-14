import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    arr_str = input().strip()

    if n == 0:
        arr = deque()
    else:
        arr = deque(arr_str[1:-1].split(','))

    reverse = False
    error_flag = False

    for cmd in p:
        if cmd == "R":
            reverse = not reverse
        elif cmd == "D":
            if not arr:
                error_flag = True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if error_flag:
        print("error")
    else:
        if reverse:
            arr.reverse()
        print("[" + ",".join(arr) + "]")