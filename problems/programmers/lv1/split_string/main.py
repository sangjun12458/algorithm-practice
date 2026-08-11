def solution(s):
    answer = 0

    x = ''
    cnt_x = 0
    cnt_not_x = 0
    for c in s:
        if x == '':
            x = c
            cnt_x += 1
        elif x == c:
            cnt_x += 1
        else:
            cnt_not_x += 1
        if cnt_x == cnt_not_x:
            x = ''
            cnt_x = 0
            cnt_not_x = 0
            answer += 1
    if x != '':
        answer += 1

    return answer