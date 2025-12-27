# 2473. 세 용액
import sys
input = sys.stdin.readline
INF = 10**9

N = int(input())
solution = list(map(int, input().split()))
solution.sort()

best = INF * 3
answer = [0, 0, 0]

for i in range(N-2):
    left = i + 1
    right = N - 1

    while left < right:
        if solution[i] < 0 and solution[right] < 0:
            total = solution[i] + solution[right-1] + solution[right]
            abs_total = abs(total)
            if abs_total < best:
                best = abs_total
                answer = [solution[i], solution[right-1], solution[right]]
            break

        if solution[i] > 0 and solution[left] > 0:
            total = solution[left] + solution[left+1] + solution[i]
            abs_total = abs(total)
            if abs_total < best:
                best = abs_total
                answer = [solution[left], solution[left+1], solution[i]]
            break

        total = solution[i] + solution[left] + solution[right]
        abs_total = abs(total)

        if abs_total < best:
            best = abs_total
            answer = [solution[i], solution[left], solution[right]]

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            answer.sort()
            print(*answer)
            sys.exit(0)

answer.sort()
print(*answer)