
def solution(n, w, num):
    answer = 0
    a = n // (2*w)
    n %= 2*w
    b = n // w
    n %= w
    
    num_a = num // (2*w)
    num_b = num_a // w
    num_c = num_a % w

    answer += num_a
    if num_b % 2 == 0:
        pass
    else:
        pass


    return answer