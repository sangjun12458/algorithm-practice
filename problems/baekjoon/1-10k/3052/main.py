nums = [0] * 42
result = 0

for _ in range(10):
    rem = int(input()) % 42 
    if nums[rem] == 0:
        nums[rem] = 1
        result += 1

print(result)