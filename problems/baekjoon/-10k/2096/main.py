# 2096. 내려가기
import sys
input = sys.stdin.readline

n = int(input().strip())
max_arr = [[0] * 3 for _ in range(2)]
min_arr = [[0] * 3 for _ in range(2)]

OLD, NEW = 0, 1

for i in range(n):
    OLD, NEW = NEW, OLD
    a, b, c= map(int, input().split())

    max_arr[NEW][0] = max(max_arr[OLD][:2]) + a
    max_arr[NEW][1] = max(max_arr[OLD]) + b
    max_arr[NEW][2] = max(max_arr[OLD][1:]) + c

    min_arr[NEW][0] = min(min_arr[OLD][:2]) + a
    min_arr[NEW][1] = min(min_arr[OLD]) + b
    min_arr[NEW][2] = min(min_arr[OLD][1:]) + c

print(max(max_arr[NEW]), min(min_arr[NEW]))