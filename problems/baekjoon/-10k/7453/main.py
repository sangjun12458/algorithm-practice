# 7453. 합이 0인 네 정수
import sys
input = sys.stdin.readline

n = int(input()) # 1 <= n <= 4000, n**4 <= 256e12
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB, CD = dict(), dict()
for a in A:
    for b in B:
        if AB.get(a+b):
            AB[a+b] += 1
        else:
            AB[a+b] = 1
for c in C:
    for d in D:
        if CD.get(c+d):
            CD[c+d] += 1
        else:
            CD[c+d] = 1

ans = 0
for s in AB:
    ans += AB[s] * CD.get(-s, 0)

print(ans)