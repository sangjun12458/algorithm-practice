# 2630. 색종이 만들기
import sys
from collections import deque
input = sys.stdin.readline
q = deque()

n = int(input().strip())
paper = [input().split() for _ in range(n)]

q.append((0, 0, n))
whites, blues = 0, 0
while q:
    x, y, l = q.popleft()
    color = paper[x][y]
    isSingleColor = True
    for i in range(x, x+l):
        for j in range(y, y+l):
            if paper[i][j] != color:
                isSingleColor = False
    if isSingleColor:
        if color == '0':
            whites += 1
        else:
            blues += 1
    else:
        if l >= 2:
            nl = l // 2
            q.append((x, y, nl))
            q.append((x, y + nl, nl))
            q.append((x + nl, y, nl))
            q.append((x + nl, y + nl, nl))

print(whites, blues, sep='\n')