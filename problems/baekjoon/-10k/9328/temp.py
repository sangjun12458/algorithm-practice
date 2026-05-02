# 9328. 열쇠
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    building = [input().strip() for _ in range(h)]
    keys = input().strip()
    
    visited = [[False] * w for _ in range(h)]
    q = deque()
    door = []
    for i in range(h):
        for j in range(w):
            if i != 0 and i != h-1 and j != 0 and j != w-1:
                continue
            q.append(i, j)
            while q:
                x, y = q.popleft()
                if visited[x][y]: continue
                visited[x][y] = True
                