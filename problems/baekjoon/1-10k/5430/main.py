import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    nums = input().strip()[1:-1]

    if nums:
        nums = nums.split(',')
    else:
        nums = []

    front, back = 0, 0
    reverse = False

    for cmd  in p:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == "D":
            if reverse:
                back += 1
            else:
                front += 1

    if front + back > len(nums):
        print("error")
    else:
        result = nums[front:len(nums)-back]
        if reverse:
            result.reverse()
        print('[' + ",".join(result) + ']')
