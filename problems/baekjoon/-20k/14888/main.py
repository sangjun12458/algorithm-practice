# 14888.

N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split())) # +, -, *, /

arr = [[0]]

stack = [(A[0], O.copy())]

while stack:
    x, opers = stack.pop()
    idx = sum(opers)
    if opers[0] > 0:
        pass
    if opers[1] > 0:
        pass
    if opers[2] > 0:
        pass
    if opers[3] > 0:
        pass

answer = 0
