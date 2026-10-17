def solution(X, Y):
    answer = ''

    ca = [0] * 10
    cb = [0] * 10
    for i in range(10):
        ca[i] = X.count(str(i))
        cb[i] = Y.count(str(i))
    for i in range(9, -1, -1):
        t = min(ca[i], cb[i])
        answer += str(i) * t

    while len(answer) >= 2 and answer[0] == '0':
        answer = answer[1:]
    if not answer:
        answer = '-1'

    return answer
