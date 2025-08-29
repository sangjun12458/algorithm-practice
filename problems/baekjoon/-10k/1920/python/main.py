import sys
input = sys.stdin.readline

n = int(input())
a = list(input().split())
m = int(input())
b = list(input().split())

d = dict()
for num in a:
    d[num] = 1

for target in b:
    if d.get(target):
        print(1)
    else:
        print(0)