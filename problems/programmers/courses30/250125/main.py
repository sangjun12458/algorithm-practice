# [PCCE 기출문제] 9번 / 이웃한 칸

def solution(board, h, w):
    answer = 0
    dh = [-1, 0, 1, 0]
    dw = [0, 1, 0, -1]
    n = len(board)
    cnt = 0
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if not (0 <= nh < n and 0 <= nw < n):
            continue
        if board[h][w] == board[nh][nw]:
            cnt += 1
    answer = cnt
    return answer