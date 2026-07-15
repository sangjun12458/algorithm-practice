def solution(cards1, cards2, goal):
    answer = ''

    p1, p2, p3 = 0, 0, 0
    while p3 < len(goal):
        if p1 < len(cards1) and goal[p3] == cards1[p1]:
            p1 += 1
            p3 += 1
        elif p2 < len(cards2) and goal[p3] == cards2[p2]:
            p2 += 1
            p3 += 1
        else:
            break

    if p1 == len(cards1)-1 and p2 == len(cards2)-1 and p3 == len(cards3)-1:
        answer = "Yes"
    else:
        answer = 'No'

    return answer