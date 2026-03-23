# 17825. 주사위 윷놀이

dice = tuple(map(int, input().split()))
board = []

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

set_board()

print(board)