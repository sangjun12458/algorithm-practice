# 10775. 공항
import sys
import heapq
input = sys.stdin.readline

g = int(input().strip())
p = int(input().strip())
planes_in_gate = [[] for _ in range(g+1)]
for i in range(1, p+1):
    planes_in_gate[int(input().strip())].append(i)

pq = []
ans = p
for gate in range(1, g+1):
    for plane in planes_in_gate[gate]:
        if gate > len(pq):
            heapq.heappush(pq, -plane)
        else:
            if plane < -pq[0]:
                ans = min(ans, -heapq.heappop(pq)-1)
                heapq.heappush(pq, -plane)
            else:
                ans = min(ans, plane-1)

print(ans)