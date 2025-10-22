# 28702. FizzBuzz
arr = [input().strip() for _ in range(3)]
for i in range(3):
    if arr[i].isnumeric():
        x = int(arr[i])
        idx = i
y = x + 3 - idx
if y % 3 == 0:
    if y % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
else:
    if y % 5 == 0:
        print('Buzz')
    else:
        print(y)