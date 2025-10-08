# 15829. Hashing
R = 31
M = 1234567891

l = int(input().strip())
s = input().strip()

hashing = 0
r = 1

for i in range(l):
    a = ord(s[i]) - ord('a') + 1
    hashing = (hashing + a * r) % M
    r = (r * R) % M
    
print(hashing)