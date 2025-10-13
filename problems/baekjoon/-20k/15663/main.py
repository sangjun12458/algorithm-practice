# 15663. N과 M (9)
from itertools import permutations

n, m = map(int, input().split())
nums = map(int, input().split())

for p in sorted(set(permutations(nums, m))):
    print(*p)