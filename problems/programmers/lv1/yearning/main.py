def solution(name, yearning, photo):
    answer = []

    d = dict()
    for i in range(len(name)):
        d[name[i]] = yearning[i]

    for p in photo:
        total = 0
        for n in p:
            total += d[n] if d.get(n) else 0
        answer.append(total)

    return answer