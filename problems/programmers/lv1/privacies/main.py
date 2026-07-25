def solution(today, terms, privacies):
    answer = []

    y, m, d = map(int, today.split('.'))
    
    e_period = dict()
    for term in terms:
        t, p = term.split(' ')
        e_period[t] = int(p)

    for idx, privacy in enumerate(privacies):
        pp, pt = privacy.split(' ')
        py, pm, pd = map(int, pp.split('.'))
        ep = e_period[pt]
        py = py + (pm + ep - 1) // 12
        pm = (pm + ep - 1) % 12 + 1
        
        today = y * 10000 + m * 100 + d
        deadline = py * 10000 + pm * 100 + pd

        if deadline <= today:
            answer.append(idx+1)

    return answer
