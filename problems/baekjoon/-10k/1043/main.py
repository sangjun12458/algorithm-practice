# 1043. 거짓말
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
knowns = list(map(int, input().split()))
persons = [False] * (n + 1)
parties = [list(map(int, input().split())) for _ in range(m)]

print(knowns)
print(persons)
print(parties)