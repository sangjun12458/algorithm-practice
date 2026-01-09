# 1202. 보석 도둑
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewel = [tuple(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

jewel.sort()
bag.sort()

heap = []
answer = []
pj = 0
for pb in range(K):
    while pj < N and jewel[pj][0] <= bag[pb]:
        heapq.heappush(heap, -jewel[pj][1])
        pj += 1
    if heap:
        answer.append(-heapq.heappop(heap))

print(sum(answer))