# 7453. 합이 0인 네 정수
import sys
input = sys.stdin.readline

n = int(input()) # 1 <= n <= 4000, n**4 <= 256e12
A, B, C, D = dict(), dict(), dict(), dict()
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A[a] = A.get(a, 0) + 1
    B[b] = B.get(b, 0) + 1
    C[c] = C.get(c, 0) + 1
    D[d] = D.get(d, 0) + 1

AB = dict()
for k1 in A:
    for k2 in B:
        AB[k1+k2] = AB.get(k1+k2, 0) + A[k1]*B[k2]

ans = 0
for k1 in C:
    for k2 in D:
        ans += AB.get(-k1-k2, 0)*C[k1]*D[k2]

print(ans)