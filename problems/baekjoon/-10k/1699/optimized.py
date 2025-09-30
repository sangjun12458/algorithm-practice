# 1699. 제곱수의 합 (라그랑주의 네 제곱수 정리)
import math

n = int(input())

def is_square(x):
    return int(math.isqrt(x))**2 == x

# 1. 제곱수인 경우
if is_square(n):
    print(1)
    exit()

# 2. 두 제곱수 합인 경우
for i in range(1, int(math.isqrt(n))+1):
    if is_square(n - i*i):
        print(2)
        exit()

# 3. 세 제곱수 판별 (라그랑주 보조 정리: 4^a(8b+7) 형태면 4개 필요)
while n % 4 == 0:
    n //= 4
if n % 8 == 7:
    print(4)
else:
    print(3)