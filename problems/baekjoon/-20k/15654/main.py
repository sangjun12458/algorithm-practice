# 15654. N과 M (5)
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0] * (n + 1)
nums.sort()

def dfs(s, depth):
    if depth == m:
        print(s.strip())
        return

    for i in range(n):
        num = nums[i]
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(s + f'{num} ', depth + 1)
        visited[i] = 0

dfs('', 0)