# 9328. 열쇠
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    building = [input().strip() for _ in range(h)]
    keys = input().strip()
    