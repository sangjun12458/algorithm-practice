# 5525. IOIOI
n = int(input())
m = int(input())
s = input()

cnt = 0
pattern = 0
i = 1

while i < m - 1:
    if s[i-1:i+2] == 'IOI':
        pattern += 1
        if pattern == n:
            cnt += 1
            pattern -= 1
        i += 2
    else:
        pattern = 0
        i += 1

print(cnt)