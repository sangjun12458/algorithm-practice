
def signals_input():
    ss = input().split(',')
    arr = []
    row = []
    for s in ss:
        a = ''
        for c in s:
            if '1' <= c <= '9':
                a += c
        if a:
            row.append(int(a))
            if len(row) >= 3:
                arr.append(row.copy())
                row.clear()
    return arr

signals = signals_input()
blinkers = [[0, 0] for _ in range(len(signals))]
answer = -1

for tick in range(2, 20**3):
    cnt = 0
    for x in range(len(signals)):
        blinkers[x][1] += 1
        if blinkers[x][1] == signals[x][blinkers[x][0]]:
            blinkers[x][0] = (blinkers[x][0] + 1) % 3
            blinkers[x][1] = 0
        if blinkers[x][0] == 1:
            cnt += 1
    if cnt == len(signals):
        answer = tick
        break

print(answer)