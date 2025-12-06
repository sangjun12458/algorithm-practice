# 1918. 후위 표기식

x = input().strip()

stack = []
result = []

priority = {
    '+': 1, '-': 1,
    '*': 2, '/': 2,
}

for c in x:
    if 'A' <= c <= 'Z':
        result.append(c)

    elif c == '(':
        stack.append(c)

    elif c == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()

    else:
        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[c]:
            result.append(stack.pop())
        stack.append(c)

while stack:
    result.append(stack.pop())

print(''.join(result))