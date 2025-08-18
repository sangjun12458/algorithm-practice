import sys
input = sys.stdin.readline

n = int(input())
m = []
for _ in range(n):
    age, name = input().split()
    m.append((int(age), name))

m.sort(key=lambda x: x[0])

for age, name in m:
    print(age, name)