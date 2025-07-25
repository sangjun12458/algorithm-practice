import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()
counter = Counter(nums)

print(round(sum(nums) / n))

print(nums[n // 2])

modes = counter.most_common() 
if len(modes) > 1 and modes[0][1] == modes[1][1]:
    print(modes[1][0])
else:
    print(modes[0][0])

print(nums[-1] - nums[0])