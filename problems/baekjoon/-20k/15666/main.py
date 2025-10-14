# 15666. N과 M (12)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))

seq = []
def dfs(i):
    for j in range(i, len(nums)):
        seq.append(nums[j])
        if len(seq) == m:
            print(*seq)
        else:
            dfs(j)
        seq.pop()
        
dfs(0)