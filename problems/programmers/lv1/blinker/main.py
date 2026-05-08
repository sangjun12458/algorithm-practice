
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

def solution(signals):
    answer = -1
    l = len(signals)
    end = 2*10**6
        
    cnts = [0] * (end+1)
    for i in range(l):
        g, y, r = signals[i]
        start = g + 1
        while start <= end:
            for j in range(start, min(start+y, end)):
                cnts[j] += 1
            start += g+y+r
    
    for tick in range(2, end):
        if cnts[tick] == l:
            answer = tick
            break
    
    return answer

signals = signals_input()
print(solution(signals))