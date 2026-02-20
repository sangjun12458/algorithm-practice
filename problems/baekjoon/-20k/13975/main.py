# 13975. 파일 합치기 3
import sys
import heapq
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    chapters = list(map(int, input().split()))
    files = []
    result = 0

    for i in range(k):
        heapq.heappush(files, (chapters[i], i, i))

    for _ in range(k-1):
        f1 = heapq.heappop(files)
        while f1[2] != files[0][1] + 1 and files[0][2] != f1[1]:
            heapq

    print(groups)


        
    print(result)