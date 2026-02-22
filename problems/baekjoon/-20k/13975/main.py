# 13975. 파일 합치기 3
import sys
import heapq
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    chapters = list(map(int, input().split()))
    sides = [[i, i] for i in range(k)]
    result = 0

    files = []
    for i in range(k-1):
        heapq.heappush(files, (chapters[i] + chapters[i+1], i, i+1))
        
    for _ in range(k-1):
        cost, left, right = heapq.heappop(files)
        start, end = sides[left][0], sides[right][1]
        while cost != chapters[start] + chapters[end]:
            heapq.heappush(files, (chapters[start] + chapters[end], start, end))
            cost, left, right = heapq.heappop(files)
            start, end = sides[left][0], sides[right][1]
        result += cost
        chapters[start] = chapters[end] = cost
        sides[start][1] = end
        sides[end][0] = start

    print(result)