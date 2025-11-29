# 9935. 문자열 폭발

a = input().strip()
b = input().strip()

ap = 0
bp = 0

while ap < len(a):
    if a[ap:ap+len(b)] == b:
        a = a[:ap] + a[ap+len(b):]
        ap = 0
    else:
        ap += 1
    
print(a)