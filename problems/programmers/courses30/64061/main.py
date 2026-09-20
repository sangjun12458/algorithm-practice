# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0

    ss = [[]]
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[0])):
            x = board[i][j]
            ss[j].append(x)
    for row in board:
        s = []
        for x in row:
            if x:
                s.append(x)            
        ss.append(s)

    basket = []
    for m in moves:
        if not ss[m]:
            continue
        x = ss[m].pop(0)
        if basket and basket[-1] == x:
            basket.pop()
            answer += 2
        else:
            basket.append(x)

    return answer