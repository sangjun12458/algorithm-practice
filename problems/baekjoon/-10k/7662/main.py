# 7662. 이중 우선순위 큐
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    dpq = []

    k = int(input())
    for _ in range(k):
        o, n = input().split()
        n = int(n)

        if o == 'I':
            dpq.append(n)
        elif o == 'D':
            if dpq:
                if n == -1:
                    dpq.remove(min(dpq))
                elif n == 1:
                    dpq.remove(max(dpq))

    if dpq:
        print(max(dpq), min(dpq))
    else:
        print('EMPTY')