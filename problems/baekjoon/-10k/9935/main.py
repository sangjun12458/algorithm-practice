# 9935. 문자열 폭발

# a = input().strip()
# b = input().strip()
N = 1_000_000
a = 'a' * (N//2) + 'b' * (N//2)
b = 'ab'

stack = []
pa = pb = 0


while pa < len(a):
    #print(pa, pb, stack)
    print(len(stack))
    if a[pa] == b[pb]:
        stack.append((b[pb], pb))
        pa += 1
        pb += 1
        if pb == len(b):
            a = a[:pa-pb] + a[pa:]
            pa -= pb
            for _ in range(len(b)):
                stack.pop()
            if stack:
                _, pb = stack[-1]
                pb += 1
            else:
                pb = 0
    else:
        pb = 0
        if a[pa] != b[pb]:
            pa += 1

# while ap < len(a):
#     if a[ap:ap+len(b)] == b:
#         a = a[:ap] + a[ap+len(b):]
#         ap = 0
#     else:
#         ap += 1

if a:
    print(a)
else:
    print('FRULA')

# mirkovC4nizCC44
# C4

# 12ab112ab2ab
# 12ab