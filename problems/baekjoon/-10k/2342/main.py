# 2342. Dance Dance Revolution
INF = 10**6

seq = list(map(int, input().split()))

ans = INF
stack = [(0, 0, 0, 0)]

while stack and False:
    left, right, depth, cost = stack.pop()
    now = seq[depth]
    if now == 0:
        ans = min(ans, cost)
        continue
    if cost + len(seq) - depth >= ans:
        continue
    
    if left == 0:
        stack.append((now, right, depth+1, cost+2))
    elif left == now or right == now:
        stack.append((left, right, depth+1, cost+1))
    else:
        if (left + 1) % 4 + 1 == now:
            stack.append((now, right, depth+1, cost+4))
        else:
            stack.append((now, right, depth+1, cost+3))
        
        if right == 0:
            stack.append((left, now, depth+1, cost+2))
        elif (right + 1) % 4 + 1 == now:
            stack.append((left, now, depth+1, cost+4))
        else:
            stack.append((left, now, depth+1, cost+3))

dp = [(-1, -1, 0)] * len(seq)
left = right = 0
cost = 0
for idx, now in enumerate(seq):
    if now == 0:
        break
    if left == now or right == now:
        cost += 1
    elif left == 0:
        left = now
        cost += 2
    elif right == 0:
        right = now
        cost += 2
    else:
        if (left + now) % 2 == 0:
            right = now
            cost += 3
        else:
            left = now
            cost += 3

print(cost)
