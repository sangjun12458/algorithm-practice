import sys
input = sys.stdin.readline

n = int(input())
nums = list()
cnts = [0 for _ in range(8001)]
for _ in range(n):
    x = int(input())
    nums.append(x)
    cnts[x + 4000] += 1
nums.sort()

mean = round(sum(nums) / n)
median = nums[n // 2]
mode = 0
first = second = 0
for i in range(len(cnts)-1, -1, -1):
    if cnts[i] >= cnts[first]:
        second = first
        first = i
if cnts[first] == cnts[second]:
    mode = second - 4000
elif cnts[first] > cnts[second]:
    mode = first - 4000
rng = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(rng)
