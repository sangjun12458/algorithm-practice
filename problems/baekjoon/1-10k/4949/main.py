import sys

input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == ".": 
        break

    stack = []
    result = "yes"
    
    for ch in sentence:
        if ch in "([":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack.pop() != "(":
                result = "no"
                break
        elif ch == "]":
            if not stack or stack.pop() != "[":
                result = "no"
                break
    
    if stack:
        result = "no"

    print(result)