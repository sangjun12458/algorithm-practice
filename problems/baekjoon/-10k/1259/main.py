# 1259. 팰린드롬 수
while True:
    x = input().strip()
    if x == '0': break
    is_pal = True
    for i in range(len(x) // 2):
        if x[i] != x[-1-i]:
            is_pal = False
            break
    print('yes' if is_pal else 'no')