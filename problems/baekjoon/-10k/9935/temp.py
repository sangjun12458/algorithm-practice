# a = input().strip()
# b = input().strip()

a = 'mirkovC4nizCC44'
b = 'C4'

stack = []
new_a = ''

pa = 0
pb = 0

while pa < len(a):
    if a[pa] == b[pb]:
        stack.append(a[pa])
        pa += 1
        pb += 1
        if pb == len(b):
            for _ in range(pb):
                stack.pop()
                pb = 0
    else:
        if a[pa] == b[0]:
            pb = 0
        else:
            new_a += a[pa]
            pa += 1

print(new_a)
print(stack)

# if a:
#     print(a)
# else:
#     print('FRULA')