# 2747. 피보나치 수
n = int(input().strip())
a, b = 0, 1
for _ in range(1, n+1):
        a, b = b, a + b
print(a)