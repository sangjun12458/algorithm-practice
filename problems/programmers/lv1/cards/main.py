def solution(cards1 : list, cards2 : list, goal : list):
    answer = 'Yes'

    p1, p2 = 0, 0
    for word in goal:
        if p1 < len(cards1) and word == cards1[p1]:
            p1 += 1
        elif p2 < len(cards2) and word == cards2[p2]:
            p2 += 1
        else:
            answer = 'No'
            break

    return answer