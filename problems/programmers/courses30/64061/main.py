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
        x = ss[m][-1]
        if basket and basket[-1] == x:
            basket.pop()
            answer += 1
        else:
            basket.append(x)

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]

answer = solution(board, moves)
print(answer)
