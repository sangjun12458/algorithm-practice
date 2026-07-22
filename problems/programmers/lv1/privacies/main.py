def solution(today, terms, privacies):
    answer = []

    y, m, d = map(int, today.split('.'))
    
    e_period = dict()
    for term in terms:
        t, p = term.split(' ')
        e_period[t] = int(p)

    for privacy in privacies:
        pp, pt = privacy.split(' ')
        py, pm, pd = map(int, pp.split('.'))
        ep = e_period[pt]
        py = py + (pm + ep) // 12
        pm = (pm + ep) % 12
        

    return answer