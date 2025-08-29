import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r, s = input().split()
    r = int(r)
    result = [ch * r for ch in s]
    print(''.join(result))