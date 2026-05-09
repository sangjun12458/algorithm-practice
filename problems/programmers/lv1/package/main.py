
def solution(n, w, num):
    answer = 0
    a = n // (2*w)
    n %= 2*w
    b = n // w
    n %= w
    
    return answer