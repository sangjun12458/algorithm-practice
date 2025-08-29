import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

up = [1]*n
down = [1]*n

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            up[i] = max(up[i], up[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if seq[j] < seq[i]:
            down[i] = max(down[i], down[j] + 1)

result = 0
for i in range(n):
    result = max(result, up[i] + down[i] - 1)

print(result)