# 9466. 텀 프로젝트
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    student = [0] + list(map(int, input().split()))

    state = [0] * (n+1)
    for i in range(1, n+1):
        start = state[i]
        if start == 2 or start == 3:
            continue

        now = student[start]
        while now == 0:
            
            now = 1