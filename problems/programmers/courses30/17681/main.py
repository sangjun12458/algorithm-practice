def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        c = a | b
        s = ""
        while c > 0:
            if c % 2:
                s += '#'
            else:
                s += ' '
            c //= 2
        s += ' ' * (n - len(s))
        s = s[::-1]
        answer.append(s)
    return answer