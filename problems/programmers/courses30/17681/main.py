def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        c = a | b
        s = ''
        while c > 0:
            if c % 2:
                s = '#' + s
            else:
                s = ' ' + s
            c //= 2
        answer.append(s)
    return answer