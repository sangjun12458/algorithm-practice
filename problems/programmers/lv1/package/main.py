
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

    # 빼낼 상자 개수 계산
    answer = height - num_height
    if r ^ num_r:
        answer += 1 if r + num_r > w else 0
    else:
        answer += 1 if r <= num_r else 0

    return answer

solution(22, 6, 8)