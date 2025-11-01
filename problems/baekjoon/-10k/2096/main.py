# 2096. 내려가기
import sys
input = sys.stdin.readline

n = int(input().strip())
max_arr = [0] * 3
min_arr = [0] * 3

for i in range(n):
    a1, b1, c1 = max_arr
    a2, b2, c2 = map(int, input().split())

    max_arr[0] = max(a1, b1) + a2
    max_arr[1] = max(max(a1, b1), c1) + b2
    max_arr[2] = max(b2, c2) + c2

    min_arr[0] = min(a1, b1) + a2
    min_arr[1] = min(min(a1, b1), c1) + b2
    min_arr[2] = min(b1, c1) + c2

print(max(max_arr), min(min_arr))