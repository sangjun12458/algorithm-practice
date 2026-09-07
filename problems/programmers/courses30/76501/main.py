def solution(absolutes, signs):
    answer = 0

    l = len(absolutes)
    for i in range(l):
        answer += absolutes[i] if signs[i] else -absolutes[i]

    return answer