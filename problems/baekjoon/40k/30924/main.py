# 30924. A+B - 10 (제2편)
import random

check = [0] * 10001
a, b = 0, 0

for _ in range(19997):
    if a == 0:
        n = random.randint(1, 10000)
        while check[n] == 1:
            n = random.randint(1, 10000)
        check[n] = 1
        print("? A", n, flush=True)
        resp = int(input().strip())
        if resp == 1:
            a = n
    else:
        n = random.randint(1, 10000)
        while check[n] == 2:
            n = random.randint(1, 10000)
        check[n] = 2
        print("? B", n, flush=True)
        resp = int(input().strip())
        if resp == 1:
            b = n
    if b != 0:
        print("!", a+b, flush=True)
        break
