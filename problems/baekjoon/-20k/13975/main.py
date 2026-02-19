# 13975. 파일 합치기 3
import sys
import heapq
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    chapters = list(map(int, input().split()))
    groups = []
    result = 0

    for i in range(k):
        heapq.heappush(groups, (chapters[i], i))

        
    print(result)