# 20303. 할로윈의 양아치

N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))
friend = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)


print(candy)
print(friend)