#. 1918. 후위 표기식

#x = input().strip()
#x = 'A*(B+C)'
x = 'A+B*C-D/E'
x = 'A*(B+C)'
x = 'A+(B*(C-D)/E)' 

def postfix(s):
    ns = ''
    sub_s = ''
    arr = []
    stack = []

    for c in s:
        if 'A' <= c <= 'Z':
            if sub_s:
                sub_s += c
            else:
                arr.append(c)
        elif c == '(':
            sub_s += c
            stack.append(c)
        elif c == ')':
            stack.pop()
            sub_s += c
            if not stack:
                arr.append(postfix(sub_s[1:-1]))
                sub_s = ''
        else:
            if sub_s:
                sub_s += c
            else:
                arr.append(c)

    new_arr = []
    oper = ''
    for c in arr:
        if c in ['/', '*']:
            oper = c
        else:
            new_arr.append(c)
            if oper:
                new_arr.append(c)
    print(arr)
    #ns = ''.join(arr)
    return ns

# for c in x:        
#     stack.append(c)
#     if 'A' <= c <= 'Z':
#         while stack:
#             if stack[-1] == '(':
#                 break
#             y += stack.pop()
#     elif c == ')':            
#         while stack:
#             if stack[-1] in ('(', ')'):
#                 stack.pop()
#             else:
#                 y += stack.pop()

print(x)
y = postfix(x)
print(y)