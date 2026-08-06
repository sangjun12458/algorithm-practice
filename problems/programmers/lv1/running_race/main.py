def solution(players : list, callings):
    from copy import deepcopy
    answer = deepcopy(players)
    ranks = dict([(name, idx) for idx, name in enumerate(answer)])

    for name in callings:
        r = ranks[name]
        ranks[name] = r-1
        ranks[answer[r-1]] = r
        answer[r-1], answer[r] = answer[r], answer[r-1]

    return answer
