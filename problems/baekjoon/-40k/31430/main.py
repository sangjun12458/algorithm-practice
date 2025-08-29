# 31430. A+B - 투 스텝
alphabet = 'abcdefghijklmnopqrstuvwxyz'
base = 26

t = int(input())
if t == 1:
    a, b = map(int, input().split())
    k = a + b
    s = ''

    while k >= base:
        remainder = k % base
        s = alphabet[remainder] + s
        k //= base

    s = alphabet[k] + s

    if len(s) < 13:
        print('a' * (13-len(s)) + s)
    else:
        print(s)
elif t == 2:
    s = input().strip()
    while len(s) > 1 and s[0] == 'a':
        s = s[1:]
    result = alphabet.index(s[0])
    for ch in s[1:]:
        result = result * base + alphabet.index(ch)

    print(result)