import sys
input = sys.stdin.readline

left = list(input().strip())
right = []

n = int(input())

for _ in range(n):
    command = input().strip()
    if command.startswith('P'):
        _, x = command.split()
        left.append(x)
    elif command == 'L':
        if left:
            right.append(left.pop())
    elif command == 'D':
        if right:
            left.append(right.pop())
    elif command == "B":
        if left:
            left.pop()
print(''.join(left + right[::-1]))
