import sys
input = sys.stdin.readline

n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

dots.sort(key=lambda x: (x[1], x[0]))

for x, y in sorted(dots, key=lambda p: (p[1], p[0])):
    print(x, y)