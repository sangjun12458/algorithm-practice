# 2467. 용액
INF = int(2*10**9)

N = int(input())
solutions = list(map(int, input().split()))

minus_p = -1 
plus_p = N
for idx, v in enumerate(solutions):
    if v < 0:
        minus_p = idx
    else:
        plus_p = idx
        break

best = INF
best_a = best_b = 0

def mix(a, b):
    global best, best_a, best_b
    if abs(a+b) < best:
        best = abs(a+b)
        best_a, best_b = a, b

if minus_p > 0:
    mix(solutions[minus_p-1], solutions[minus_p])

if plus_p < N-1:
    mix(solutions[plus_p], solutions[plus_p+1])
 
while minus_p >= 0 and plus_p < N:
    mix(solutions[minus_p], solutions[plus_p])
    if -solutions[minus_p] > solutions[plus_p]:
        plus_p += 1
    else:
        minus_p -= 1

print(best_a, best_b)