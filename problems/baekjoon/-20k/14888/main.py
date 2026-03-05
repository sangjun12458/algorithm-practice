# 14888. 연산자 끼워넣기
INF = 1_000_000_000

N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split())) # +, -, *, /

arr = [[0]]
stack = [(A[0], O.copy())]
max_v = -INF
min_v = INF

while stack:
    x, (a, b, c, d) = stack.pop()
    s = sum([a, b, c, d])
    if s == 0:
        max_v = max(x, max_v)
        min_v = min(x, min_v)
        continue

    y = A[N - s]
    if a > 0:
        stack.append((x + y, [a - 1, b, c, d]))
    if b > 0:
        stack.append((x - y, [a, b - 1, c, d]))
    if c > 0:
        stack.append((x * y, [a, b, c - 1, d]))
    if d > 0:
        z = abs(x) // abs(y)
        stack.append((z if x * y > 0 else -z, [a, b, c, d - 1]))
    
print(max_v)
print(min_v)