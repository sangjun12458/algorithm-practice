# 13975. 파일 합치기 3
import sys
import heapq
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    chapters = list(map(int, input().split()))
    result = 0

    files = []
    for i in range(k-1):
        heapq.heappush(files, (chapters[i] + chapters[i+1], i, i+1))
        
    for _ in range(k-1):
        cost, start, end = heapq.heappop(files)
        while cost != chapters[start] + chapters[end]:
            heapq.heappush(files, (chapters[start] + chapters[end], start, end))
            cost, start, end = heapq.heappop(files)
        result += cost
        chapters[start] = chapters[end] = cost

    print(result)