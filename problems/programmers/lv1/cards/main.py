def solution(cards1, cards2, goal):
    answer = ''

    checked = [(0, 0)] * len(goal)
    p = 0

    for g in goal:
        print(cards1.index(g))

    return answer