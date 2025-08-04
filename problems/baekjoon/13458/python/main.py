import sys
input = sys.stdin.readline

n = int(input())
test_rooms = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
for students in test_rooms:
    result += 1
    remaining = students - b
    if remaining > 0:
        result += (remaining + c - 1) // c
        
print(result) 