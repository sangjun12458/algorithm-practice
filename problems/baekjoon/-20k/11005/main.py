# 11005. 진법 변환 2
n, b = map(int, input().split())

digits = []
while n > 0:
    r = n % b
    if r < 10:
        digits.append(str(r))
    else:
        digits.append(chr(ord('A') + r - 10))
    n //= b

print("".join(reversed(digits)))