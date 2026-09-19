# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0

    ss = [[]]
    for b in board:
        s = []
        for x in b:
            if x:
                s.append(x)            
        ss.append(s)

    basket = []
    for m in moves:
        if not ss[m]:
            continue
        x = ss[m].pop()
        if basket and basket[-1] == x:
            basket.pop()
            answer += 2
        else:
            basket.append(x)

    return answer