# 2473. 세 용액
INF = 10**9

N = int(input())
solution = list(map(int, input().split()))

# N = 5000
# neg = [-10**9 + i for i in range(2498)]
# mid = [-2, -1, 3]
# pos = [10**9 - 2499 + i for i in range(2499)]
# solution = neg + mid + pos
solution.sort()

best = INF * 3
ans = (-1, -1, -1)

while len(solution) >= 3:
    s1 = solution.pop()
    if s1 < 0:
        total = s1 + solution[-1] + solution[-2]
        if abs(total) < abs(best):
            best = total
            ans = (solution[-2], solution[-1], s1)
            break
    base = -s1//2
 
    #s2, s3 = -INF, INF
    left, right = -1, len(solution)
    #print(s1, left, right)
    for idx, s in enumerate(solution):
        if s > base:
            right = idx
            break
        left = idx
    
    if left == -1:
        total = s1 + solution[0] + solution[1]
        if abs(total) < abs(best):
            best = total
            ans = (solution[0], solution[1], s1)
    elif right == len(solution):
        total = s1 + solution[-1] + solution[-2]
        if abs(total) < abs(best):
            best = total
            ans = (solution[-2], solution[-1], s1)
    else:
        while left >= 0 and right < len(solution):
            s2 = solution[left]
            s3 = solution[right]
            total = s1 + s2 + s3
            if abs(total) < abs(best):
                best = total
                ans = (s2, s3, s1)
            if abs(s2 - base) < abs(s3 - base):
                left -= 1
            else:
                right += 1

print(*ans)