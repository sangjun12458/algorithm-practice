# 1202. 보석 도둑
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewel = [tuple(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

jewel.sort(key = lambda x: (-x[1], x[0]))
bag.sort(reverse=True)

answer = []
a, b = 0, 0
while a < N and b < K:
    weight = jewel[a][0]
    value = jewel[a][1]
    limit = bag[b]

    a += 1
    b += 1

for i in range(K):
    weight = bag[i]
    start = 0
    while start < N and jewel[start][0] > weight:
        start += 1
    answer.append(jewel[start][1])

print(jewel)
print(bag)
print(answer)