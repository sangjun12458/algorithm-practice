def solution(participant, completion):
    answer = ''

    d = dict()
    for p in participant:
        if d.get(p):
            d[p] += 1
        else:
            d[p] = 1
    for c in completion:
        d[c] -= 1
    for name, x in d.items():
        if x:
            answer = name
            break

    return answer