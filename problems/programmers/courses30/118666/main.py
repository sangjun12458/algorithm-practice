def solution(survey, choices):
    answer = ''

    idcs = [0] * 4
    for i in range(len(survey)):
        x = survey[i]
        score = choices[i] - 4
        if x == "RT" or x == "TR":
            idcs[0] += score if x == "RT" else -score
        elif x == "CF" or x == "FC":
            idcs[1] += score if x == "CF" else -score 
        elif x == "JM" or x == "MJ":
            idcs[2] += score if x == "JM" else -score
        elif x == 'AN' or x == "NA":
            idcs[3] += score if x == "AN" else -score

    answer += 'R' if idcs[0] <= 0 else 'T'
    answer += 'C' if idcs[1] <= 0 else 'F'
    answer += 'J' if idcs[2] <= 0 else 'M'
    answer += 'A' if idcs[3] <= 0 else 'N'

    return answer