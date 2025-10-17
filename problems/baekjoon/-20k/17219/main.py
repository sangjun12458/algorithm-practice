# 17219. 비밀번호 찾기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sites = dict()

for _ in range(n):
    site, password = input().split()
    sites[site] = password

for _ in range(m):
    print(sites[input().strip()])