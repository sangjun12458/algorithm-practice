# 23656. Jack and Jill

def solve():
    low, high = 1, 10**9
    steps = 0
    
    while True:
        q = int(input().strip())
        steps += 1

        if steps >= 30 and low <= q <= high:
            print("=", flush=True)    
            return
        if steps > 100:
            return

        mid = (low + high) // 2
        if q > mid:
            high = min(high, q - 1)
            print("<", flush=True)
        else:
            low = max(low, q + 1)
            print(">", flush=True)

solve()