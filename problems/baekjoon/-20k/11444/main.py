# 11444. 피보나치 수 6
import sys
sys.setrecursionlimit(10**6)
DIVISOR = 1000000007
n = int(input())

arr = []

while n > 0:
    if n % 2 == 0:
        arr.append(n+1)
        arr.append(n-1)
    else:
        arr.append(n//2+1)
        arr.append(n//2)
    n //= 2

print(arr)
print(len(arr))


# for i in range(n - 1):
#     a, b = b, (a+b)%DIVISOR

def pibo(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    elif x % 2 == 0:
        return pibo(x+1) - pibo(x-1)
    else:
        return (pibo(x//2)**2 + pibo(x//2+1)**2) % DIVISOR
    