# 1389. 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
friends = [[True] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a][b] = friends[b][a] = True
    