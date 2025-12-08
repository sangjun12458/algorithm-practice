# 2448. 별 찍기 - 11
import math
TRI = ["  *  ", " * * ", "*****"]

n = int(input())
k = int(math.log2(n // 3))

arr = []

def func(r, c, d):
    if d == k:
        arr.append((r, c, d))
    else:
        nd = d + 1
        nr = r * 2
        nc = c * 2
        func(nr, nc+1, nd)
        func(nr+1, nc, nd)
        func(nr+1, nc+2, nd)

func(0, 0, 0)

grid = [[] for _ in range(2**k)]
for r, c, _ in arr:
    grid[r].append(c)

answer = []

for row in grid:
    for i in range(3):
        s = ""
        for c in row:
            s += (" "*(3*c) + TRI[i])[len(s):]
        answer.append(s)

for ans in answer:
    print(ans + " "*(len(answer[-1])-len(ans)))