# 30804. 과일 탕후루
n = int(input().strip())
fruits = list(map(int, input().split()))
result = 0
for i in range(9):
    for j in range(9):
        nums = [0] * 10
        for k in range(i, j+1):
            nums[fruits[k]] += 1
        cnt = 0
        for k in range(1, 10):
            if nums[k] > 0:
                cnt += 1
        if cnt <= 2:
            result = max(result, j - i + 1)
print(result)