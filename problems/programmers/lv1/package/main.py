
def solution(n, w, num):
    answer = 0
    
    # 전체 택배의 높이
    sh1 = n // (2*w)
    r = n % (2*w)
    sh2 = r // w
    r %= w

    height = 2 * sh1 + sh2

    # 원하는 택배의 높이
    num_sh1 = num // (2*w)
    num_r = num % (2*w)
    num_sh2 = num_r // w
    num_r %= w

    num_height = 2 * num_sh1 + num_sh1 + (1 if num_r else 0)
    num_idx = w - num_r if num_sh2 else num_r-1

    answer = num_height - height

    return answer