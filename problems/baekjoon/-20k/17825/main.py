# 17825. 주사위 윷놀이
import sys
sys.setrecursionlimit(10**6)

dice = tuple(map(int, input().split()))
board = []
piece = [0, 0, 0, 0]
answer = 0
movable = [True] * 4

def set_board():
    global board
    for i in range(20):
        board.append((i * 2, [i+1]))
    board.append((40, [-1]))
    board[5][1].append(21)
    board.extend([(13, [22]), (16, [23]), (19, [29])]) # west: 10->13->16->19->25
    board[10][1].append(24)
    board.extend([(22, [25]), (24, [29])]) # south: 20->22->24->25
    board[15][1].append(26)
    board.extend([(28, [27]), (27, [28]), (26, [29])]) # east: 30->28->27->26->25
    board.extend([(25, [30]), (30, [31]), (35, [20])]) # north: 25->30->35->40

def dfs(depth, score):
    global answer, piece
    if depth >= 10: # 종료 조건
        answer = max(answer, score)
        return    
    if score + 40 * (10-depth) <= answer: # 가지치기
        return
    for i in range(4):
        if piece[i] == -1:
            continue
        # 움직일 위치 계산 + 파란색 칸 고려
        init_pos = piece[i]
        pos = board[init_pos][1][-1]
        cnt = 1
        while pos != -1 and cnt < dice[depth]:
            pos = board[pos][1][0]
            cnt += 1
        # 다른 말과 같은 위치이면 선택하지 않도록 구현
        keep = True
        for j in range(4):
            if i != j and pos == piece[j]:
                keep = False
        if not keep and pos != -1:
            continue
        # 도착 여부에 따라 구분
        piece[i] = pos
        if pos == -1:
            dfs(depth+1, score)
        else:
            dfs(depth+1, score + board[pos][0])
        piece[i] = init_pos

set_board()
dfs(0, 0)
print(answer)