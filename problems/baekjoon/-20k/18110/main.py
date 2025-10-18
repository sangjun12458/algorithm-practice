# 18110. solved.ac
import sys
input = sys.stdin.readline

n = int(input().strip())
levels = [0] * 31
exc = int(n * 0.15) + (1 if (n * 0.15) % 1 >= 0.5 else 0)

for _ in range(n):
    levels[int(input().strip())] += 1

for i in range(exc):
    for j in range(1, 31):
        if levels[j] > 0:
            levels[j] -= 1
            break
    
    for j in range(30, 0, -1):
        if levels[j] > 0:
            levels[j] -= 1
            break

total = 0
for i in range(1, 31):
    total += i * levels[i]

if n == 0:
    print(0)
else:
    result = total / (n - 2 * exc)
    print(int(result) + (1 if result % 1 >= 0.5 else 0))