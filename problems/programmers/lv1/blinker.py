
def signals_input():
    ss = input().split(',')
    l = []
    for s in ss:
        a = ''
        for c in s:
            if '1' <= c <= '9':
                a += c
        if a:
            l.append(a)
    signals = []
    return l

signals = signals_input()

print(signals)