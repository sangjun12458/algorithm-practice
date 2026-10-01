def solution(k, m, score : list):
    answer = 0

    score.sort(reverse=True)
    t = len(score) // m
    for i in range(t):
        answer += score[i*m+2] * m

    return answer
