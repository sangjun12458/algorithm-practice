# 2239. 스도쿠

def dfs(depth):
    global exist_answer
    if exist_answer: return
    if depth == len(blank):
        global ans
        ans = ["".join(map(str, row)) for row in sudoku]
        exist_answer = True
        return

    r, c = blank[depth]
    numbers = [True] * 10
    numbers[0] = False
    for i in range(9):
        numbers[sudoku[i][c]] = False
    for j in range(9):
        numbers[sudoku[r][j]] = False
    
    start_i = r//3*3
    start_j = c//3*3
    for i in range(start_i, start_i+3):
        for j in range(start_j, start_j+3):
            numbers[sudoku[i][j]] = False

    for number, useable in enumerate(numbers):
        if useable:
            sudoku[r][c] = number
            dfs(depth+1)
            sudoku[r][c] = 0

sudoku = [[] for _ in range(9)]
#counts = [0] * 10
blank = []
for i in range(9):
    row = input()
    for j, x in enumerate(row):
        x = int(x)
        sudoku[i].append(x)
        if x == 0:
            blank.append((i, j))
        #counts[x] += 1

exist_answer = False
ans = []
dfs(0)
for row in ans:
    print(row)