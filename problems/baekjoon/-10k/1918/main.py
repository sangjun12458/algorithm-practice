#. 1918. 후위 표기식

x = input().strip()
#x = 'A*(B+C)'
y = ''

stack = []

for c in x:        
    stack.append(c)
    if 'A' <= c <= 'Z':
        while stack:
            if stack[-1] == '(':
                break
            y += stack.pop()
    elif c == ')':            
        while stack:
            if stack[-1] in ('(', ')'):
                stack.pop()
            else:
                y += stack.pop()

print(x)
print(y)