# 1562. 계단 수

DIVISOR = 1_000_000_000

N = int(input())

arr = [[0] * 10 for _ in range(N+1)]
for i in range(1, 10):
    arr[1][i] = 1

for digit in range(1, N):
    arr[digit+1][0] = (arr[digit][0] + arr[digit][1]) % DIVISOR
    arr[digit+1][9] = (arr[digit][8] + arr[digit][9]) % DIVISOR
    for i in range(2, 9):        
        arr[digit+1][i] = (arr[digit][i-1] + arr[digit][i] + arr[digit][i+1]) % DIVISOR

print(arr)

print(sum(arr[N]) % DIVISOR)