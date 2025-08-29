# 30917. A+B - 10 (제1편)
for i in range(1, 10):
    print("? A", i, flush=True)
    resp = int(input())
    if resp == 1:
        a = i
    print("? B", i, flush=True)
    resp = int(input())
    if resp == 1:
        b = i
print("!", a+b)