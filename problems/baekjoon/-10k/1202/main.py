# 1202. 보석 도둑
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewel = [tuple(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]
visited = [0] * K

jewel.sort(key = lambda x: -x[1])
bag.sort()

answer = []
for i in range(N):
    weight = jewel[i][0]
    value = jewel[i][1]

    for j in range(K):
        if not visited[j] and weight <= bag[j]:
            visited[j] = True
            answer.append(value)
            break

print(sum(answer))