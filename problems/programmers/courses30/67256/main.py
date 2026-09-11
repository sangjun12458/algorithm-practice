def solution(numbers, hand):
    answer = ''

    lh = -1
    rh = -1

    for n in numbers:
        if n in [1, 4, 7]:
            lh = n
            answer += 'L'
        elif n in [3, 6, 9]:
            rh = n
            answer += 'R'
        else:
            pass
GIT A
    return answer