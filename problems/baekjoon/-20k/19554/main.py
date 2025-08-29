# 19554. Guess the number

n = int(input().strip())

l = 1
r = n

for _ in range(50):
    mid = (l + r) // 2
    print("?", mid, flush=True)
    resp = int(input().strip())

    if resp == -1:
        l = mid + 1
    elif resp == 0:
        print("=", mid, flush=True)
        break
    elif resp == 1:
        r = mid - 1