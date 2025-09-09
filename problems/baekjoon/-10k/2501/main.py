# 2501. 약수 구하기
import sys
import math
input = sys.stdin.readline
n, k = map(int, input().split())
divisors = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        divisors.append(i)
        if i != n // i:
            divisors.append(n // i)

divisors.sort()

if len(divisors) < k:
    print(0)
else:
    print(divisors[k-1])