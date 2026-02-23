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
    for c in chapters:
        heapq.heappush(files, c)

    for _ in range(k-1):
        f1 = heapq.heappop(files)
        f2 = heapq.heappop(files)
        heapq.heappush(files, f1 + f2)
        result += f1 + f2

    print(result)