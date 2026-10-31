# dot product

def solution(a, b):
    answer = 1234567890
    result = 0
    for x, y in zip(a, b):
        result += x * y
    answer = result
    return answer