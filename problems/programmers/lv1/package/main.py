
def solution(n, w, num):
    answer = 0
    a = n // (2*w)
    n %= 2*w
    b = n // w
    n %= w
    
    num_a = num // (2*w)
    num_b = num_a // w
    num_c = num_a % w


    return answer