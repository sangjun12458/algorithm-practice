def solution(food):
    answer = ''

    for idx, x in enumerate(food):
        if idx == 0:
            continue
        answer += str(idx) * (x // 2)
    answer = answer + '0' + answer[::-1]

    return answer