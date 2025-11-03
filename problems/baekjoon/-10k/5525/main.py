# 5525. IOIOI
n = int(input())
m = int(input())
s = input()

p = 'IO' * n + 'I'
cnt = 0
for i in range(m - 2*n):
    j = i + 2*n + 1
    if s[i:j] == p:
        cnt += 1

print(cnt)