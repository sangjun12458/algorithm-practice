# 28277. 뭉쳐야 산다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) 
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return

    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    size[b] = 0

n, q = map(int, input().split())
parent = list(range(n))
size = [0] * n

for i in range(n):
    data = list(map(int, input().split()))
    k = data[0]
    size[i] = k

for _ in range(q):
    command = input().split()
    if command[0] == '1':
        a, b = int(command[1]) - 1, int(command[2]) - 1
        union(a, b)
    else:
        x = int(command[1]) - 1
        print(size[find(x)])