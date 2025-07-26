import sys
input = sys.stdin.readline

n, x = map(int, input().split())
print(" ".join(num for num in input().split() if int(num) < x))