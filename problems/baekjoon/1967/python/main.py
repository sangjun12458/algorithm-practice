import sys
sys.setrecursionlimit(10**6)
sys.stdin.readline

n = int(input())
graph = [[] for _ in range(10001)]

for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))

result = 0

def dfs(root):
    global result
    
    maxlen = 0
    for child, weight in graph[root]:
        if graph[child]:
            sublen = dfs(child) + weight
        else:
            sublen = weight
        result = max(result, sublen + maxlen)
        maxlen = max(maxlen, sublen)
    
    return maxlen

dfs(1)

print(result)