from itertools import permutations

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))

for p in permutations(nums, m):
    print(*p)