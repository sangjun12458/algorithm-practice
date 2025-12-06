#. 1918. 후위 표기식

x = input().strip()

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
            if oper:
                new_arr[-1] = new_arr[-1] + c + oper
                oper = ''
            else:
                new_arr.append(c)

    oper = ''
    for c in new_arr:
        if c in ['+', '-']:
            oper = c
        else:
            ns += c
            if oper:
                ns += oper
                oper = ''

    return ns

y = postfix(x)
print(y)