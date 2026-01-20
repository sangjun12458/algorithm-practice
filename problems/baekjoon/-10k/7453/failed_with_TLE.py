# 7453. 합이 0인 네 정수
import sys
input = sys.stdin.readline

n = int(input()) # 1 <= n <= 4000
A, B, C, D = dict(), dict(), dict(), dict()
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A[a] = A.get(a, 0) + 1
    B[b] = B.get(b, 0) + 1
    C[c] = C.get(c, 0) + 1
    D[d] = D.get(d, 0) + 1

AB = dict()
for a, ca in A.items():
    for b, cb in B.items():
        AB[a+b] = AB.get(a+b, 0) + ca * cb

ans = 0
for c, cc in C.items():
    for d, cd in D.items():
        ans += AB.get(-c-d, 0) * cc * cd

print(ans)