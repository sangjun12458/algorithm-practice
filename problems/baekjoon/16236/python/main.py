import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
fishes = []
shark = 2
total_time = 0

for i in range(n):
    for j in range(n):
        if space[i][j] in range(1, 7):
            fishes.append((i, j, space[i][j]))

while True:
    feed = -1

    
        
        




print(total_time)
