# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0

    ss = [[] for _ in range(len(board)+1)]
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[0])):
            x = board[i][j]
            if x:
                ss[j+1].append(x)

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
