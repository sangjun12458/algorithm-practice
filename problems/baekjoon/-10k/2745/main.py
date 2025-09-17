# 2745. 진법 변환

n, b = input().split()
b = int(b)

print(int(n, b))

# 직접구현

# n, b = input().split()
# b = int(b)

# result = 0
# for i, ch in enumerate(n[::-1]):  # 뒤에서부터
#     if ch.isdigit():
#         value = int(ch)
#     else:
#         value = ord(ch) - ord('A') + 10
#     result += value * (b ** i)

# print(result)