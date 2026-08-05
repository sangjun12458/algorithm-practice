def solution(players : list, callings):
    from copy import deepcopy
    answer = deepcopy(players)

    ranks = [0] * len(players)

    for c in callings:
        i = answer.index(c)
        answer[i-1], answer[i] = answer[i], answer[i-1]

    return answer