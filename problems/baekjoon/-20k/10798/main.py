# 10798. 세로읽기

x = [input().strip() for _ in range(5)]
s = ''
l = 0
for word in x:
    l = max(l, len(word))
for i in range(l):
    for word in x:
        if len(word) > i:
            s += word[i]

print(s)