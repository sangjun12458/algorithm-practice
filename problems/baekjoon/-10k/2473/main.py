# 2473. 세 용액

N = int(input())
solution = list(map(int, input().split()))
solution.sort()

print(solution)

ab = []

start = 0
end = N-1

while start < end:
    ab.append(solution[start] + solution[end])
    if abs(solution[start]) < abs(solution[end]):
        end -= 1
    else:
        start += 1

print(ab)