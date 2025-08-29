# 8958. OX퀴즈
t = int(input())
for _ in range(t):
    s = input().strip()
    count = 0
    result = 0
    for c in s:
        if c == "O":            
            count += 1
            result += count
        else:
            count = 0
    print(result)