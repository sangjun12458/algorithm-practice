# 9935. 문자열 폭발

a = input().strip()
b = input().strip()
l = len(b)

stack = []

for c in a:
    stack.append(c)
    if len(stack) >= l and "".join(stack[-l:]) == b:
        del stack[-l:]

result = "".join(stack)
print(result if result else "FRULA")