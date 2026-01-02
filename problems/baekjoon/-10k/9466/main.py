# 9466. 텀 프로젝트
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    student = [0] + list(map(int, input().split()))

    state = [0] * (n+1)
    position = [0] * (n+1)
    turn = 0
    answer = 0

    for start in range(1, n+1):
        now = start
        if state[now] != 0:
            continue
        
        turn += 1
        state[now] = turn
        position[now] = 1

        while state[student[now]] == 0:
            position[student[now]] = position[now] + 1
            now = student[now]
            state[now] = turn

        if state[student[now]] == turn:
            answer += position[student[now]] - 1
        else:
            answer += position[now]

    print(answer)