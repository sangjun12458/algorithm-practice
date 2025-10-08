# 15829. Hashing
R = 31
M = 1234567891

l = int(input().strip())
s = input().strip()

hashing = 0
for i in range(l):
    hashing += (s[i] * (R ** i))
print(hashing)