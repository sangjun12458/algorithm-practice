# 2744. 대소문자 바꾸기

s = input().strip()

ns = ""
for c in s:
    if 'a' <= c <= 'z':
        ns += c.upper()
    elif 'A' <= c <= 'Z':
        ns += c.lower()

print(ns)