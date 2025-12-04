# 11444. 피보나치 수 6
import sys
sys.setrecursionlimit(10**6)
DIVISOR = 1000000007
n = int(input())

def fibo(k):
    def mul(a, b):        
        ab00 = (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % DIVISOR
        ab01 = (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % DIVISOR
        ab10 = (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % DIVISOR
        ab11 = (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % DIVISOR
        return [[ab00, ab01], [ab10, ab11]]

    if k == 1:
        m = [[1, 1], [1, 0]]
        return m
    elif k % 2 == 0:
        half = fibo(k//2)
        return mul(half, half)
    else:
        m = [[1, 1], [1, 0]]
        return mul(m, fibo(k - 1))
    
print(fibo(n)[1][0])