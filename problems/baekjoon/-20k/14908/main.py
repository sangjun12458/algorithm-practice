# 14908. 구두 수선공
import sys
input = sys.stdin.readline

n = int(input().strip())
jobs = []
for i in range(1, n+1):
    t, s = map(int, input().split())
    jobs.append((t, s, i))

jobs.sort(key=lambda x: (-x[1] / x[0], x[2]))

print(" ".join(str(job[2]) for job in jobs))