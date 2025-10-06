# 30802. 웰컴 키트
import sys
input = sys.stdin.readline

n = int(input().strip())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = 0
for s in shirts:
    cnt += s // t
    if s % t > 0:
        cnt += 1
print(cnt)
print(n // p, n % p)