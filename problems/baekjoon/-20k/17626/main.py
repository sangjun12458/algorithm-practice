# 17626. Four Squares
import math
n = int(input().strip())

def is_square(x):
    return int(math.sqrt(x)) ** 2 == x

if is_square(n):
    print(1)
    exit()

for i in range(1, int(math.sqrt(n)) + 1):
    if is_square(n - i * i):
        print(2)
        exit()

while n % 4 == 0:
    n //= 4
if n % 8 == 7:
    print(4)
else:
    print(3)