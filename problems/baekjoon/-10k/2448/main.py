# 별 찍기 - 11
import math

n = int(input())

def triangle(n, k, r):
    if k == 0:
        print(f'{"*":^5}')
        print(f'{"* *":^5}')
        print('*****')
    else:
        #nk = k // 2
        triangle(n, k - 1, r)
        triangle(n, k - 1, r - (k - 1) * 6)
        triangle(n, k - 1, r + (k - 1) * 6)

k = int(math.log2(n // 3))
triangle(n, k, k * 6)