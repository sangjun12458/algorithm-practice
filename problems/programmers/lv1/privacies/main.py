def solution(today, terms, privacies):
    answer = []

    y, m, d = map(int, today.split('.'))
    
    e_period = dict()
    for term in terms:
        t, p = term.split(' ')
        e_period[t] = int(p)

    for privacy in privacies:
        py, pm, pd = map(int, privacy.split('.'))

    return answer