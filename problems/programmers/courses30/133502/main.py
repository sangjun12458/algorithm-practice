def solution(ingredient):
    answer = 0

    s = []
    for i in ingredient:
        s.append(i)
        if len(s) < 4:
            continue
        if s[-1] == s[-4] == 1 and s[-3] == 2 and s[-2] == 3:
            answer += 1
            for _ in range(4):
                s.pop()

    return answer