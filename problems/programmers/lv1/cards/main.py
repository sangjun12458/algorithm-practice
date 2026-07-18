def solution(cards1, cards2, goal):
    answer = ''
    l1, l2, l3 = len(cards1), len(cards2), len(goal)
    p1, p2, p3 = 0, 0, 0
    while p3 < l3 and (p1 < l1 or p2 < l2):
        if p1 < l1 and goal[p3] == cards1[p1]:
            p1 += 1
            p3 += 1
        elif p2 < l2 and goal[p3] == cards2[p2]:
            p2 += 1
            p3 += 1
        else:
            p1 += 1
            p2 += 1
            
    if p1 == len(cards1) and p2 == len(cards2) and p3 == len(goal):
        answer = "Yes"
    else:
        answer = 'No'

    return answer