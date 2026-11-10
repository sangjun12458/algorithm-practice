def solution(answers):
    answer = []

    a_arr = [1, 2, 3, 4, 5]
    b_arr = [2, 1, 2, 3, 2, 4, 2, 5]
    c_arr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a, b, c = 0, 0, 0
    ca, cb, cc = 0, 0, 0
    for x in answers:
        if x == a_arr[a]:
            ca += 1
        if x == b_arr[b]:
            cb += 1
        if x == c_arr[c]:
            cc += 1
        a = (a + 1) % 5
        b = (b + 1) % 8
        c = (c + 1) % 10

    answer = [1]
    c_max = ca
    if cb > c_max:
        answer = [2]
        c_max = cb
    elif cb == c_max:
        answer.append(2)
    if cc > c_max:
        answer = [3]
    elif cc == c_max:
        answer.append(3)

    return answer