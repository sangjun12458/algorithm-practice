def solution(babbling):
    answer = 0

    poss = ['aya', 'ye', 'woo', 'ma']
    for b in babbling:
        s = 0
        prev = ''
        isPossible = True
        while s < len(b):
            if b[s:s+2] in ['ye', 'ma'] and prev != b[s:s+2]:
                prev = b[s:s+2]
                s += 2
            elif b[s:s+3] in ['aya', 'woo'] and prev != b[s:s+3]:
                prev = b[s:s+3]
                s += 3
            else:
                isPossible = False
                break
        if isPossible:
            answer += 1

    return answer