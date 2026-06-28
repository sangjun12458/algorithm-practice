def solution(s, skip, index):
    answer = ''

    for x in s:
        if s not in skip:
            x = (x - 'a' + index) % 26 + 'a'
        answer += x

    return answer