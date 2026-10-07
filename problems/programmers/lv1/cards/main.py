def solution(cards1 : list, cards2 : list, goal : list):
    answer = ''

    s1, s2 = 0, 0
    result = 'Yes'
    for word in goal:
        if word in cards1[s1:]:
            idx = cards1[s1:].index(word)
            s1 = idx + 1
        elif word in cards2[s2:]:
            idx = cards2[s2:].index(word)
            s2 = idx + 1
        else:
            result = "No"
            break
        
    answer = result
    return answer