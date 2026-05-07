import math

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
l = len(signals)
end = 10**6
# for i in range(l):
#     end = math.lcm(end, sum(signals[i]))


cnts = [0] * (end+1)
for i in range(l):
    g, y, r = signals[i]
    start = g + 1
    while start <= end:
        for j in range(start, min(start+y, end)):
            cnts[j] += 1
        start += g+y+r

answer = -1
for tick in range(2, end):
    if cnts[tick] == l:
        answer = tick
        break
print(answer)