# 10986. 나머지 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

prefix = 0
remainder_count = [0] * m
remainder_count[0] = 1
cnt = 0

for num in nums:
    prefix = (prefix + num) % m
    cnt += remainder_count[prefix]
    remainder_count[prefix] += 1

print(cnt)
