# 15654. N과 M (5)
n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
visited = [False] * n
seq = []

def dfs():
    if len(seq) == m:
        print(*seq)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        seq.append(nums[i])
        dfs()
        seq.pop()
        visited[i] = False

dfs()