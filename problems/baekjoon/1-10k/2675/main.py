import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r, s = input().split()
    r = int(r)
    new_str = ''
    for ch in s:
        for _ in range(r):
            new_str += ch
    
    print(new_str)