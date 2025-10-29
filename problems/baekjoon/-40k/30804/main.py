# 30804. 과일 탕후루
import sys
input = sys.stdin.readline

n = int(input().strip())
fruits = list(map(int, input().split()))

result = 0
for i in range(1, 10):
    for j in range(1, 10):
        cnt = 0
        for f in fruits:
            if f == i or f == j:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 0
print(result)