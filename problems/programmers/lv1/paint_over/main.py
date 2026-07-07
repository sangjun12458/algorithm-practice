def solution(n, m, section):
    answer = 0

    start = section[0]
    answer += 1
    for s in section[1:]:
        s_num = int(s)
        end = start + m - 1
        if s_num <= end:
            continue
        else:
            start = s_num
            answer += 1

    # preprocess
    # while True:
    #     # paint
    #     break

    return answer