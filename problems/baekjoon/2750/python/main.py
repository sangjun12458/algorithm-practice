import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

sys.stdout.write('\n'.join(map(str, nums)) + '\n')
