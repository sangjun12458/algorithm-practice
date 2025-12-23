# 2342. Dance Dance Revolution
INF = 10**6

seq = list(map(int, input().split()))

dp = [(-1, -1, 0)] * len(seq)

left = 0
right = 0
cost = 0

for now in seq:
    if now == left:
        cost += 1
    elif now == right:
        cost += 1
    else:
        pass

ans = INF
def dfs(left, right, depth, cost):
    if depth == len(seq):
        ans = min(ans, cost)
        return
    if cost + len(seq) - depth > ans:
        return
    
    now = seq[depth]
    if left == 0:
        dfs(now, right, depth+1, cost+2)
    elif left == now or right == now:
        dfs(left, right, depth+1, cost+1)
    else:
        

dfs(0, 0, -1, 0)
